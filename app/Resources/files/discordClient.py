# Older code, typed in a hurry, dont mind Errors
# Please keep note i left some commands out
# Ignore blank strings, those are tokens
from colorama import Fore, Style
from discord.ext import commands
import discord
import requests
import json
import time
import random
import threading
import database

prefix: str = "$" ## Bot prefix .startswith("$")

welcome: int = 755183664832315412 ## Welcome channel ID
leave: int = 755184273270767656 ## Leave channel ID

owner: int = 443156642213920779 ## Owner ID (Me)

bot = commands.Bot(command_prefix=prefix, case_insensitive=True) ## Client
bot.remove_command('help') ## Removes help from the cog

bearer: str = ""
basicauth: str = ""
bot_id: str = ""

## -----------------
## Tokens for using |
## and interacting  |
## with the ifunny  |
## api              |
## -----------------

def randcolor() -> hex: ## Generates a random Hexidecimal Integer (Color Code)
    random_number: int = random.randint(0, 0xffffff)
    return random_number


def build_headers(bearer=False) -> dict:
    header: dict = {} ## Builds headers for interacting with iFunny api
    if bearer: header["Authorization"] = "Bearer " + bearer
    else: header["Authorization"] = "Basic " + basicauth
    return header

def user_by_nick(user) -> dict: ## Gets an iFunny user by thier Nickname
    url: str = f"https://api.ifunny.mobi/v4/users/by_nick/{user}"
    r = requests.get(url, headers=build_headers()).json()
    return r

async def send(ctx, message) -> None: ## An embeded Send function
    embedVar: discord.Embed = discord.Embed( ## For sending pretty messages
        description=message, color=randcolor()) ## Generated random color
    await ctx.send(embed=embedVar)              ## For prettier messages

async def logger(ctx) -> None:
    await ctx.message.delete() ## Deletes messages and prints command
    print(Fore.BLUE + ctx.message.author.name + ": ", ## To the terminal
        Fore.LIGHTMAGENTA_EX + ctx.message.content + Style.RESET_ALL)

async def basic_data(data) -> discord.Embed:
    embedVar: discord.Embed = discord.Embed(description="Data",
        color: int =randcolor()) ## Iterates over a dictionary
    for key in data.get("data"): ## And adds a iterated data to the
        embedVar.add_field(name=key, ## EmbedVar
            value=json.dumps(data.get("data")[key], indent=4), inline=False)
    return embedVar

@bot.command()
async def help(ctx) -> None: ## New help cog that isnt ugly as f***
    commands: list = []
    for key in bot.commands: ## Iterates over commands and checks name
        commands.append(key.name)
    message: str = "Commands:\n\n" + "\n".join(commands)
    await send(ctx, message)

@bot.command()
async def verify(ctx, *args) -> None: ## Verify command
    #await logger(ctx)
    user: discord.Member = ctx.message.author
    dis: int = database.get_user_by_discord(str(user.id)) ## Checks database
                                                          ## For iFunny id
    if dis:                                               ## Against discord id
        return await send(ctx, "You are already verified")

    database.delete_user(str(user.id))
    if len(args) < 3: ## Checks arguments to make sure its accurate
        return await send(ctx, f"Please state it like this\n\n{prefix}verify " \
        f"YourAge Gender iFunnyName\n\nEX:\n{prefix}verify 17 Male Tobi")


    if int(args[0]) < 16 or int(args[0]) > 99: ## Checks if they are above 16
        try:                                   ## and under the age of 99
            return await ctx.guild.ban(ctx.message.author,
                reason=f"User was {args[0]} years old")
        except Exception as Error: ## bans user and listens for exception
            return await send(ctx, str(Error))
    else: pass
    roles: list = []
    f : str = "Female" ## Male var
    m: str = "Male"    ## Female var
    genders: dict = {"m": m , "male": m, "boy": m, "guy": m,
               "f": f, "female": f, "girl": f, "gal": f}
    ## Genders dict for checking common works
    if int(args[0]) < 18: roles.append("JailBait")
    else: roles.append("Fuckable") ## Adds roles to list based on age

    gender = genders.get(args[1].lower())
    if not gender: ## Checks gender against gender dict
        return await send(ctx,
            f"You must use a gender:\n\nEX:\n{prefix}verify 17 male Tobi")
    else:
        roles.append(gender)


    data: dict = user_by_nick(args[2]) ## Gets user by their nick :))
    status: int = data.get("status")
    if status != 200:
        return await send(ctx, f"{args[2]} has no iFunny account")
    else:
        user_id: (None, str) = data.get("data").get("id")
        nick: (None, str) = data.get("data").get("nick")
        days: (None, int) = data.get("data").get("meme_experience").get("days")
        if days < 7: ## Checks if their days are above 7
            return await send(ctx,
                "You must have an iFunny account for a week to verify")


    new: (None, int) = database.get_user_by_ifunny(user_id)

    if new: ## Checks database against iFunny id
        return await send(ctx,
            "This user is already verified...\n\n(if something went wrong," \
                "please reach out to admins)")
    else:
        database.insert_user(str(user.id), user_id)


    await send(ctx, f"Confirmed as {nick}!")

    await ctx.author.edit(nick=nick)

    roles.append("Default")
    roles.append("Plebs")
    roles.append("Music") ## More default roles

    for role in roles: ## iterates over role names and adds said role
        await user.add_roles(discord.utils.get(ctx.guild.roles, name=role))

@bot.command(pass_context: bool =True)
@commands.has_role('admins') ## Checks if role Admins
async def delete(ctx, member: discord.Member):
    await logger(ctx) ## Deletes a user from From database and unroles them
    user: discord.Member = member
    roles: list = [i.name for i in user.roles if i.name != "@everyone"]
    database.delete_user(str(user.id)) ## Deletes database ID and gets roles ^^
    await user.edit(nick=user.name)
    for role in roles: ## Iterates over roles and removes them
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name=role))
    await send(ctx, f"{user.name} has been unverified!")

@bot.command()
@commands.has_role('admins')
async def say(ctx): ## Says your arguments
    message: str = ctx.message.content.replace("$say", "", 1)
    await send(ctx, message)

@bot.command()
async def unverify(ctx):
    await logger(ctx)
    try: ## Unverifys on user lever
        user: discord.Member = ctx.message.author ## Member object
        roles: list = [i.name for i in user.roles if i.name != "@everyone"]
        database.delete_user(str(user.id)) ## Gets roles and deletes database
        await user.edit(nick=user.name)    ## Entry, then edits nickname
        for role in roles: ## Iterates over roles, and then removes the roles
            await user.remove_roles(discord.utils.get(ctx.guild.roles, name=role))
        await send(ctx, "You have been unverified!")
    except Exception as Error: ## Listens for exception
        await send(ctx, str(Error))

@bot.command()
async def data(ctx, args):
    await logger(ctx) ## Sends a json string of iFunny user data
    return await send(ctx, json.dumps(user_by_nick(args), indent=4))

@bot.command()
async def profile(ctx, user: discord.Member = None):
    # Finish later :p
    if user == None:
      user: discord.Member = ctx.author
    server = ctx.guild

    ## ---------
    ## Will get|
    ## info on |
    ## a users |
    ## discord |
    ## account |
    ## --------

@bot.event
async def on_ready(): ## Sets bot status to "Streaming Movies"
    await bot.change_presence(activity=discord.Streaming(name="Movies", url="TWITCH URL"))

@bot.event
async def on_member_join(member):
    ## Listens for member join and sends a message to welcome channel
    embedVar: discord.Embed = discord.Embed( ## creates embed
        description=f"{member.name} has joined the server!", color=randcolor())
    channel = bot.get_channel(welcome) ## gets welcome channel
    await channel.send(embed=embedVar) ## Sends Embed variable

@bot.event
async def on_member_remove(member):
    ## Listens for member leave and sends a message to leave channe
    embedVar: discord.Embed = discord.Embed( ## Creates embed
        description=f"{member.name} has left the server!", color=randcolor())
    channel = bot.get_channel(leave)   ## Gets leave channel
    await channel.send(embed=embedVar) ## sends embed variable

def times_used(string, term):
    return len(string.split(term)) - 1 ## Times used function for amount of
                                       ## times a string has been used
                                       ## within a string
@bot.event
async def on_message(message): ## Replaces default on message init
    await bot.process_commands(message) ## and replaces with custom one

@bot.command()
async def user(ctx, args): ## Gets an iFunny users json data and
    embedV = await basic_data(user_by_nick(args)) ## Sends it to a channel
    await ctx.send(embed=embedV)

def start(api_key): ## Prints output and Runs the Bot
    print(Fore.LIGHTMAGENTA_EX + 'Discord bot is online' + Style.RESET_ALL)
    bot.run(api_key)


## ------------------------
## This is an example for  |
## a discord management bot|
## This is designed to be  |
## age restrictive, and    |
## while i removed a few   |
## commands for this       |
## particular entry        |
## to conserve space it    |
## does a good job at its  |
## purpose, managing the   |
## discord server          |
## ------------------------

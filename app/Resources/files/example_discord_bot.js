const Discord = require('discord.js'); // This imports the Discord JS api module

const bot = new Discord.Client(); // This initializes a Client object with the name bot

var Prefix = "!"; // This defines the bots prefix ``!help``

var commands = {}; // This is a dictionary to store functions in

var token = "lol no you cant have my token"; // This is the bots API token

class  ctxParser {
  constructor(args, Message) { // This creates a parsing
      let message = Message;   // Class for easier access
      this.channel = message.channel; // to variables
      this.author = message.author;   // without having a
      this.args = args;               // a mess of code
  }
}


function processMessage(Message) {
    let fullCommand = Message.content.substr(1);
    let splitCommand = fullCommand.split(" ");
    let primaryCommand = splitCommand[0]; // This parses the message content into variables
    var args = splitCommand.slice(1);     // for arguments to be parsed
    const ctx = new ctxParser(args, Message); // into this ctx parsing object


    if (commands[primaryCommand] != undefined) { // This checks if the function for the command they called exists
          console.log("Command received: " + Message.content);
          commands[primaryCommand](ctx) // This calls on that object and runs it with the parser as the argument
    }

    else {
        ctx.channel.send("That is not one of my commands"); // This raises an exception to the user end
    }
}

bot.on('message', (Message) => {
    if (Message.author == bot.user) {
        return; // This makes sure the bot doesnt respond to itself
    }

    if (Message.content.startsWith(Prefix)) {
        processMessage(Message); // This starts the command processing
    }
})

commands["help"] = Help; // This adds the help command to the dictionary
function Help(ctx) { // This defines the help command and accepts the CTX argument
    ctx.channel.send("test");
}

bot.on('ready', () => {
    console.log("Bot is online!");
}) // This tells you when the bot is connected

bot.login(token); // This logs into the bot

//----------------------------------------------
//{                                              |
//  "name": "JS Discord Bot",                    |
//  "version": "1.0.0",                          |
//  "description": "Discord bot env in NodeJS",  |
//  "dependencies": {                            |
//    "discord.js": "^12.3.1"                    |
//  },                                           |
//  "author": "Tobi"                             |
//}                                              |
//-----------------------------------------------

//--------------
// This is my   |
// package.json |
// content      |
//--------------

//--------------------
// This is an example |
// discord bot written|
// in NodeJS using    |
// Atom text editor   |
// and the discord.js |
// framework.         |
//--------------------
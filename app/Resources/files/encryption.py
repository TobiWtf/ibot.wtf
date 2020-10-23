import sqlite3 as sqlite
import time
import base64
from cryptography.fernet import Fernet


##-----------------------------
## Functions of execute        |
## fetchall, and fetch one     |
## can be found in database.py |
## they are ran through sqlite3|
## ----------------------------


ENCRYPT_KEY = b'49787B672952587B6A484A545E4F474C52752B3046686661574A237B424A44' \
              b'3D7B2D6A4D4C496956527A4E76324E6F3765524D3F47527A504233553C43525248795236256E'

## ------------------
## This is an example|
## encryption key    |
## from fernet which |
## has been encoded  |
## into bytes and    |
## then stored       |
##-------------------

def get_bytes(string):
    return bytes(string, encoding="UTF-8")

def encode(key):
    return base64.b16encode(base64.b85encode(base64.a85encode(key)))

    ## Encodes multiple times

def decode(key):
    return base64.a85decode(base64.b85decode(base64.b16decode(key)))

    ## Decodes multiple times

def cipher():
    key = decode(ENCRYPT_KEY)
    return Fernet(key) ## Cipher object

def encrypt(key): ## Encrypts data
    return cipher().encrypt(get_bytes(key)).decode("utf-8")

def decrypt(key): ## Decrypts data
    return cipher().decrypt(get_bytes(key)).decode("utf-8")

def create_table_bearers():
    execute("CREATE TABLE bearers (user_id TEXT, bearer TEXT)")
    ## Creates a table for storing Bearer tokens

def logout(user_id):
    execute("DELETE FROM bearers WHERE user_id=?", (user_id,))
    ## Deletes a bearer from database for logging out

def login(user_id, bearer):
    logout(user_id) ## Slides bearer token into database
    execute("INSERT INTO bearers VALUES (?, ?)", (user_id, encrypt(bearer)))

def get_bearer(user_id):
    bearer = fetchone("SELECT bearer FROM bearers WHERE user_id=?", (user_id,))
    if not bearer: ## Gets a bearer of arg[user_id]
        return None
    else: return decrypt(bearer[0])

def nickname_key():
    with open(r"libs/text_files/nickname_key.txt", "r") as file:
        data = file.read()
    return data

def new_nickname_key():
    def key():
        return encode(get_bytes(str(time.time()))).decode("utf-8")

    with open(r"libs/text_files/nickname_key.txt", "w") as file:
        file.write(key())

## -------------------------
## The querys above are used|
## for putting encrypted    |
## data into the database   |
## and then retrieves the   |
## database, and the last   |
## two methods, make a key  |
## used for checking against|
## a thread and one method  |
## that creates a new key   |
## -------------------------

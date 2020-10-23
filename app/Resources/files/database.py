import sqlite3
import random

connection: str = "test.db" ## Connection file String

def executeMany(args: list = []) -> None:
    try:
        with sqlite3.connect(connection) as database: ## Establishes connection
            for query in args: ## iterates through arguments
                cursor = database.cursor() ## Establishes a cursor object
                cursor.execute(*query) ## Executes the query from iterated item
                cursor.close() ## Closes the cursor
    except Exception as Error: ## Cataches Exception
        print(str(Error)) ## Prints exception and passes

def execute(*args) -> None: ## None is the Object type it returns
    try:
        with sqlite3.connect(connection) as database: ## Establishes connection
            cursor = database.cursor() ## Establishes a cursor object
            cursor.execute(*args) ## Executes the query from args tuple
            cursor.close() ## Closes the cursor
        return ## Closes connection and returns object type None
    except Exception as Error: ## Cataches Exception
        print(str(Error)) ## Prints exception and passes


def fetchall(*args) -> (None, tuple): ## Claims it will return None or Tuple
    try:
        with sqlite3.connect(connection) as database: ## Establishes connection
            cursor = database.cursor() ## Establishes a cursor object
            data: (None, tuple) = cursor.execute(*args).fetchall()
                            ## Fetches all from *args query ^^^^
            cursor.close() ## Closes the cursor
        return data ## Closes connection and returns object of types tuple or
                    ## None ^
    except Exception as Error: ## Cataches Exception
        print(str(Error)) ## Prints exception and passes



def fetchone(*args) -> (None, tuple):  ## Claims it will return None or Tuple
    try:
        with sqlite3.connect(connection) as database: ## Establishes connection
            cursor = database.cursor() ## Establishes a cursor object
            data: (None, tuple) = cursor.execute(*args).fetchone()
                            ## Fetches one from *args query ^^^^
            cursor.close() ## Closes the cursor
        return data ## Closes connection and returns object of types tuple or
                    ## None ^
    except Exception as Error: ## Cataches Exception
        print(str(Error)) ## Prints exception and passes

def fetchmany(size: int, *args) -> (None, tuple): ## Claims it will
                                                  ## return None or Tuple
    try:
        with sqlite3.connect(connection) as database: ## Establishes connection
            cursor = database.cursor() ## Establishes a cursor object
            data: (None, tuple) = cursor.execute(*args).fetchmany(size)
                            ## Fetches many from *args query using
                            ## size argument ^^^^
            cursor.close() ## Closes the cursor
        return data ## Closes connection and returns object of types tuple or
                    ## None ^
    except Exception as Error:
        print(str(Error))

def get(numOne: int, numTwo: int) -> int: ## Initializes funtion with int ATW
    return random.randint(numOne, numTwo) ## Returns random integer


def test() -> None: ## Returns none
    execute("CREATE table test_table (column_1 TEXT, column_2 TEXT)")
    ## This creates a table name test_table in our test.db ^^

    list_of_exec: list = [] ## List of executables for testing
    for i in range(get(1, 3)): ## iterates over list of random values
        list.append(("INSERT INTO test_table VALUES (?, ?)", ## appends query
            (str(get(1, 10)), get(1, 10)))) ## to the list_of_exec for later use

    executeMany(list_of_exec) ## Calls execute many function for list_of_exec

    results: (None, tuple) = fetchall("SELECT * FROM test_table") ## Recalls
                                                                  ## data ^

    print(results) ## Prints results

if __name__ == "__main__": ## Checks name of script vs Main and starts it
    test() ## calls on test function


## --------------------------
## This is an example of how |
## Sqlite3 can be used as    |
## a database to open and    |
## then close a connection   |
## this works best for Async |
## enviroments where you     |
## cannot run an async module|
## this also works with      |
## multi threading use       |
## with caution, it is fairly|
## optimized but it is by no |
## means perfect and i would |
## need an actual Database   |
## to make this better       |
## --------------------------

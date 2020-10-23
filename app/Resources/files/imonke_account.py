from imonke import iMonkeRequest, iMonkeHandler

request = iMonkeRequest.requests()
url = iMonkeHandler.iMonkeUrl()
json = iMonkeHandler.json()

## --------------------
## This gets the       |
## modules from one    |
## location to keep    |
## things consolidated |
##---------------------

me_endpoint = url + "me/"
user_endpoint = url + "user/"
auth_endpoint = url + "auth/"


def create_user(email, password, nick, bio=None):

    ## Creates a user profile

    headers = {"email": email, ## Creates a dict object of params
                "nick": nick,
                "password": password}

    general_error = "Please include all params (email, nick, password)"
    bio_warning = "You may include a bio as well" ## Error strings <^^

    if not bio:
        iMonkeHandler.raise_warning(bio_warning) ## Raises warning of not
        pass                                     ## having a bio
    else:
        headers['bio'] = bio # Sets bio param to bio argument

    try:
        data = request.post(user_endpoint, data=json.dumps(headers)) ## Makes
        return data.json()                                       ## A request
    except Exception as Error:                                ## To make account
        raise Error


def get_me(bearer):
    header = {"Authorization": "Bearer " + bearer} ## Creates dict of params
    try:
        data = request.get(me_endpoint, headers=header) ## Gets data
        return data.json() ## Converts json string to pythonic format
    except Exception as Error:
        raise Error


def auth(email, password=None, secret=None):

    general_error = "You must provide a secret or a password"
    gen_error_2 = "Only password OR secret please" ## General warnings <^^

    if not secret and not password:
        iMonkeHandler.raise_warning(general_error)
    else:
        pass
    header = {"email": email, }
    if secret:
        header['secret'] = secret

    if password:
        header['password'] = password

    ## ------------------------
    ## This makes sure that we |
    ## The right params in the |
    ## headers, as to fetch    |
    ## an auth token on the    |
    ## imonke.gastroden.io     |
    ## you are required to     |
    ## have a password or      |
    ## secret :))              |
    ## ------------------------

    if password and secret:
        iMonkeHandler.raise_warning(gen_error_2)

    try:
        data = request.post(auth_endpoint, json.dumps(header)) ## fetches data
        return data.json() ## Returns data in pythonic form
    except Exception as Error:
        raise Error

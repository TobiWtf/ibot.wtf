import threading

def nick_by_id(id_list, bearer=None):
    nick_list = []
    tasks = []

    if bearer:
        headers = {"Authorization": "Bearer " + bearer}
    else:
        headers = {"Authorization": "Basic " + basic}

    def get_user_data(user_id):
        url = f"{ifunny_host}/users/{user_id}"
        r = requests.get(url, headers=headers).json()
        if r["status"] == 200:
            nick_list.append(r["data"]["nick"])
        else:
            nick_list.append(f'<Unknown User>')

    [tasks.append(threading.Thread(target=get_user_data, args=(i,))) for i in id_list]
    [i.start() for i in tasks]
    [i.join() for i in tasks]

    return nick_list


## -------------------------
## Antoher script based off |
## of iFunny user Affects   |
## code, with headers       |
## building and full list   |
## comprehension used       |
## with threading to quickly|
## get a list of nicknames  |
## -------------------------

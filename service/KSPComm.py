
def login():
    import requests

    base_url = 'http://35.223.167.128:32116'
    auth_ath = "/oauth/token"
    url = base_url + auth_ath
    username = "admin"
    password = "password"
    abc = "ksp"
    client_id = abc
    client_secret = abc
    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    scriptData = {'grant_type': 'password',
                  'username': username,
                  'password': password,
                  'client_id': client_id,
                  'client_secret': client_secret}

    response = requests.post(url, headers=header, data=scriptData)
    print(response.text)
    response.raise_for_status()
    pass


def get_user(clustername, username, password):
    pass
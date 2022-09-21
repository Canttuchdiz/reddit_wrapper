import requests

#organize layout for wrapper after getting wrapper how-to info

class CredentialsError(Exception):
    def __init__(self):
        self.message = "Credentails are invalid"

    def __str__(self):
        return self.message

class Reddit ():

    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.__token = 0

        self.__token_checker()


    def __collect_data(self):
        base_url = 'https://www.reddit.com/'
        data = {'grant_type': 'password', 'username': self.username, 'password': self.password}
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': f'api-wrapper by Canttuchdiz'}, auth=auth)
        d = r.json()
        return d['access_token']

#credential exception or identifier if token not recieved

    def __token_checker(self):
        if isinstance(self.__token, int):
            data = self.__collect_data()
            self.__token = data

    def meme_gen(self):
        r = requests.get('https://reddit.com/r/memes.json')
        return r.json()

# need to change all header informations

    def user_data(self):
        token = 'bearer ' + self.__token
        base_url = 'https://oauth.reddit.com'
        headers = {'Authorization': token, 'User-Agent': 'api-wrapper by Canttuchdiz'}
        response = requests.get(base_url + '/api/v1/me', headers=headers)

        if response.status_code == 200:
            print(response.json()['name'], response.json()['comment_karma'])

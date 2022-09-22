from imports import *

#organize layout for wrapper after getting wrapper how-to info

class Reddit ():

    def __init__(self, client_id, client_secret, username, password, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = user_agent
        self._token = None

        self._token_checker()


    def _collect_data(self):
        base_url = 'https://www.reddit.com/'
        data = {'grant_type': 'password', 'username': self.username, 'password': self.password}
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': f'{self.user_agent}'}, auth=auth)
        try:
            d = r.json()
            return d['access_token']
        except KeyError:
            raise CredentialsError
            quit()

#credential exception or identifier if token not recieved

    def _token_checker(self):
        if self._token is None:
            data = self._collect_data()
            self._token = data

    def meme_gen(self):
        token = 'bearer ' + self._token
        headers = {'Authorization': token, 'User-Agent': 'api-wrapper by Canttuchdiz'}
        r = requests.get('https://reddit.com/r/memes.json', headers=headers)
        return r.json()

# need to change all header informations



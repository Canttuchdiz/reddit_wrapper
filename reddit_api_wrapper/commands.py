from imports import *

class Commands(BaseClass):
    def user_data(self):
        token = 'bearer ' + self._token
        base_url = 'https://oauth.reddit.com'
        headers = {'Authorization': token, 'User-Agent': 'api-wrapper by Canttuchdiz'}
        response = requests.get(base_url + '/api/v1/me', headers=headers)

        if response.status_code == 200:
            print(response.json()['name'], response.json()['comment_karma'])

    def meme_gen(self):
        token = 'bearer ' + self._token
        headers = {'Authorization': token, 'User-Agent': 'api-wrapper by Canttuchdiz'}
        r = requests.get('https://reddit.com/r/memes.json', headers=headers)
        return r.json()
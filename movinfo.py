from config import TmdApi
import requests


class TheMovieDb():

    def __init__(self):
        self.api = TmdApi()

    def get(self, **kwargs):
        try:
            request = kwargs['request']
        except KeyError:
            request = 'discover/movie?primary_release_year=2019'
        response = requests.get(self.api.url+request, headers=self.api.headers)
        return response.content

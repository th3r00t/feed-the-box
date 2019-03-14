import requests
from bs4 import BeautifulSoup
import json


class TorrentSearch():

    def __init__(self):
        self.search = None

    def do_search(self, q):
        search = "https://thepiratebay.rocks/search/%s/1/99/200" % (q)
        html = self.html(search)
        self.search = q
        self.results(html)

    @staticmethod
    def html(search):
        return requests.get(search)

    @staticmethod
    def print(html):
        bowl = BeautifulSoup(html.content, 'html5')
        print(bowl.find('div',{'id': 'content'}))
        return

    def results(self, html):
        bowl = BeautifulSoup(html.content, 'lxml')
        content = bowl.select('.detName')
        holding = []
        for tag in content:
            parent = tag.find_parent()
            siblings = parent.fetchNextSiblings()
            title = tag.text
            url = tag.contents[1].attrs['href']
            magnet = tag.next_sibling.next_sibling.attrs['href']
            seeders = siblings[0].text
            leechers = siblings[1].text
            result = {
                'title': title,
                'url': url,
                'magnet': magnet,
                'seeders': seeders,
                'leechers': leechers
                }
            holding.append(result)
        with open('debug/'+self.search+'.json', 'w') as file:
            json.dump(holding, file)
        return holding



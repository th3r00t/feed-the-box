import requests
from bs4 import BeautifulSoup
import json
import time
import os
from download import MagnetDownloader
class TorrentSearch():

    def __init__(self):
        self.search = None

    def do_search(self, q):
        search = "https://thepiratebay.rocks/search/%s/1/99/200" % (q)
        html = self.html(search)
        self.search = q
        return self.results(html)

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
            torrent = ""
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

    def print_results(self, results, **kwargs):
        down_links = {}
        try:
            setnum = kwargs['set']
        except KeyError:
            setnum = 1
        h, w = os.popen('stty size', 'r').read().split()
        setsize = round((int(h) / 3) - 3)
        for i, r in enumerate(results):
            if (i < setsize * setnum):
                if int(r['seeders']) < 1:
                    i = i + 1
                    pass
                else:
                    print(i, r['title'] + ' ' + r['seeders'] + ' ' + 'seeders')
                    print(r['url'])
                    down_links[i] = r['magnet']
                    i = i + 1
                if i == setsize * setnum:
                    print('Please Choose a #, or n for Next, p for Previous Sets')
                    choice = input()
                    print('Is this a (m)ovie, (t)v show, or (o)ther?')
                    dl_type = input()
                    if choice == 'n' or choice == 'N':
                        setnum = setnum + 1
                    elif choice == 'p' or choice == 'P':
                        setnum = setnum - 1
                    else:
                        # Entry point for downloading of torrent
                        choice = int(choice)
                        MagnetDownloader(down_links[choice], dl_type)
                        # print(down_links[choice])


import requests
from bs4 import BeautifulSoup



class TorrentSearch():

    def __init__(self):
        self.search = None

    def do_search(self, q):
        search = "https://thepiratebay.rocks/search/%s/1/99/200" % (q)
        html = self.html(search)
        self.search = q
        # self.print(html)
        self.write_html(html)

    @staticmethod
    def html(search):
        return requests.get(search)

    @staticmethod
    def print(html):
        bowl = BeautifulSoup(html.content, 'html5lib')
        print(bowl.find('div',{'id': 'content'}))
        return

    def write_html(self, html):
        bowl = BeautifulSoup(html.content, 'lxml')
        content = bowl.select('.detName')
        holding = []
        for tag in content:
            parent = tag.find_parent()
            holding.append(parent)
        with open('debug/'+self.search+'.html', 'w') as file:
            file.write('<table>')
            for result in holding:
                file.write('<tr>')
                file.writelines(result.prettify())
                file.write('</tr>')
            file.write('</table>')


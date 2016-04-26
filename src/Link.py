__author__ = 'Lambert Justo'

from bs4 import BeautifulSoup
import requests
from src.Entry import Entry


class Link(Entry):
    def __init__(self, _url):
        Entry.__init__(self, _url)
        if "www.reddit.com" in _url:
        	soup = BeautifulSoup(requests.get(self.get_text(), headers = {'User-agent': 'shortlistProg'}).content, "html.parser")
        else:
        	soup = BeautifulSoup(requests.get(self.get_text()).content, "html.parser")
        # extract title from url
        try:
            self._title = str(soup.title.string).strip().encode("cp437", "ignore")
        except AttributeError:
        	print("current page does not have a title")
        	self._title = _url.encode("cp437", "ignore")
        except UnicodeEncodeError:
            print("cannot output UTF-8 on this machine")
            # self._title = self._title.encode("cp437", "ignore")

    def get_title(self):
        return self._title.decode("cp437", "ignore")


from googlesearch import *
import urllib.request as urllib
from bs4 import BeautifulSoup

import readFile as rf
import readWebsite as rw
import checkPlagiat as cp

import wikipedia

def main(content):

    for i in content:
        try:

            for j in search('"' + i + '"', tld="de", num=4, stop=10, pause=2):
                clean_html = rw.readWebsite(j)
                print(cp.checkPlagiat(i, clean_html, j))

        except BaseException as err:

            try:
                wikipedia.set_lang("de")
                wikis = wikipedia.search(i[0:300])
                for j in wikis:
                    test = wikipedia.page(j)
                    clean_html = rw.readWebsite(test.url)
                    print(cp.checkPlagiat(i, clean_html, j))

            except BaseException as err:
                print(err)
                continue
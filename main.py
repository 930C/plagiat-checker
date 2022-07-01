from googlesearch import *
import urllib.request as urllib
import re
from bs4 import BeautifulSoup

import readFile as rf
import readWebsite as rw
import checkPlagiat as cp



content = rf.readFile("./testfiles/mytext.txt")

for i in content:
    try:
        for j in search('"' + i + '"', tld="de", num=4, stop=10, pause=2):
            try:
                clean_html = rw.readWebsite(j)
                print(cp.checkPlagiat(i, clean_html, j))
            except BaseException as err:
                print(err)
                continue


    except BaseException as err:
        print(err)
        try:
            url = "https://www.krone.at/themen/prozessor"
            clean_html = rw.readWebsite(url)
            print(cp.checkPlagiat(i, clean_html, url))
        except BaseException as err:
            print(err)
            continue
from googlesearch import search
import urllib.request as urllib
import re
from bs4 import BeautifulSoup

import readFile as rf
import readWebsite as rw
import checkPlagiat as cp

content = rf.readFile("./testfiles/mytext.txt")
content = content.replace("\n", "").split(".")[0:-1]

for i in content:
    for j in search(i, tld="de", num=4, stop=10, pause=2):
        try:
            clean_html = rw.readWebsite(j)
            print(cp.checkPlagiat(i, clean_html))
        except BaseException as err:
            print(err)
            continue
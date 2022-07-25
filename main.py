from googlesearch import *
import urllib.request as urllib
from bs4 import BeautifulSoup

import readFile as rf
import readWebsite as rw
import checkPlagiat as cp
import sentenceSplitter as ss

import wikipedia

def main(eingabe):
    plagiate = []

    content = ss.splitter(eingabe)

    for i in content:
        try:
            # raise BaseException()
            for j in search('"' + i + '"', tld="de", num=4, stop=10, pause=2):
                clean_html = rw.readWebsite(j)
                plagiate.append(cp.checkPlagiat(i, clean_html, j))

        except BaseException as err:
            try:
                wikipedia.set_lang("de")
                wikis = wikipedia.search(i[0:300])
                for j in wikis[0:5]:
                    test = wikipedia.page(j)
                    clean_html = rw.readWebsite(test.url)

                    checkResult = cp.checkPlagiat(i, clean_html, j)
                    if checkResult != None:
                        checkResult[1] += "(Quelle: Wikipedia)"
                        plagiate.append(checkResult)
                        break

            except BaseException as err:
                print(err)
                continue

    return plagiate
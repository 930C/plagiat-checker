from googlesearch import *
import urllib.request as urllib
from bs4 import BeautifulSoup

import readFile as rf
import readWebsite as rw
import checkPlagiat as cp
import sentenceSplitter as ss

import wikipedia

def main(eingabe, ui=None):
    plagiate = []
    content = ss.splitter(eingabe)

    for index, value in enumerate(content):
        try:
            # raise BaseException()
            for j in search('"' + value + '"', tld="de", num=1, stop=5, pause=5):
                pageContent = rw.readWebsite(j)
                checkResult = cp.checkPlagiat(value, pageContent, j)

                if checkResult != None:
                    plagiate.append(checkResult)
                    break

        except BaseException as err:
            try:
                wikipedia.set_lang("de")
                wikis = wikipedia.search(value[0:300])
                for j in wikis[0:5]:
                    pageContent = rw.readWebsite(wikipedia.page(j).url)
                    checkResult = cp.checkPlagiat(value, pageContent, j)

                    if checkResult != None:
                        checkResult[1] += "(Quelle: Wikipedia)"
                        plagiate.append(checkResult)
                        break

            except BaseException as err:
                print(err)
                continue
        finally:
            if (ui != None):
                ui.progress(int((index+1)*100/len(content)))
    return plagiate

if __name__ == "__main__":
    myString = "In a similar fashion, Arch ships the configuration files provided by upstream with changes limited to distribution-specific issues like adjusting the system file paths. It does not add automation features such as enabling a service simply because the package was installed. Packages are only split when compelling advantages exist, such as to save disk space in particularly bad cases of waste. GUI configuration utilities are not officially provided, encouraging users to perform most system configuration from the shell and a text editor."
    print(main(myString))
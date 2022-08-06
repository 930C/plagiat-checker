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
    content = ss.splitter(eingabe)              # split the input into sentences

    for index, value in enumerate(content):     # go through each sentence
        try:
            for j in search(value, tld="de", num=1, stop=5, pause=5):       # make a google search with the given sentence, in google.de, show 1 result, stop after 5 results and take a break every 5 seconds
                try:
                    pageContent = rw.readWebsite(j)                         # read the websites html and return the cleaned up content of the page
                    checkResult = cp.checkPlagiat(value, pageContent, j)    # check for plagiarism

                    if checkResult != None:
                        plagiate.append(checkResult)                        # Add the incident to the list of plagiarisms
                        break
                except BaseException as err:
                    print("Error while trying to reach " + j + " : " +  str(err))   # Website was unable to reach (HTTP 304 Error e.g.)

        except BaseException as err:    # If google search is not working and shows message "too many requests", then try wikipedia alternatively
            try:
                wikipedia.set_lang("de")
                wikis = wikipedia.search(value[0:299])  # make a wikipedia search (max of 300 letters allowed) and retrieve a list of wikipedia page titles
                for j in wikis:                         # go through each title (max 10 according to definition of wikipedia.search())
                    page = wikipedia.page(j, auto_suggest=False)    # Open the wikipedia page  - IMPORTANT: auto_suggest is set to False because a exact match between page title and term j is needed
                    url = page.url                                  # Gives the url of that wiki page
                    pageContent = rw.readWebsite(url)               # Read from the wiki page
                    checkResult = cp.checkPlagiat(value, pageContent, j)    # Check if the sentence has been copied

                    if checkResult != None:
                        checkResult[1] += " (Quelle: Wikipedia)"
                        plagiate.append(checkResult)
                        break

            except BaseException as err:
                print(err)
                continue
        finally:
            if (ui != None):
                ui.progress(int((index+1)*100/len(content)))    # For each sentence finished, increment the loading bar by a fraction
    return plagiate

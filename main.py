#!/usr/bin/env python3
# from googlesearch import search
from googleapi import google
import urllib.request as urllib
import re
from bs4 import BeautifulSoup

def checkPlagiat(sentence, html):
    


#############
# Open File -> Save all Sentences in a list

# fileDestination = input("Please input your file Location: \n>")

try:
#    f1 = open(fileDestination, "r")
    f1 = open("./testfiles/mytext.txt", "r")
    content = f1.read()
    f1.close()
except BaseException as err:
    print(f"Fehler {err}")

print(content.replace("\n", "").split(".")[0:-1])

##########################
# Start google search ->  Make a search query for each sentence and save it to a variable
# for j in search("Moderne Programmierkonzepe", tld="de", num=1, stop=10, pause=2):
searchResults = google.search("Modern Programmierkonzepte")
for j in searchResults:
    print(j)

##########################
# Open Link and read html
    site = urllib.urlopen(j)
    sitebytes = site.read()
    html = sitebytes.decode("utf8")
    site.close()
    clean_html = re.sub("<.*?>", " ", html)
    clean_html = re.sub(r"\s+", " ", clean_html)
    print(clean_html)
    checkPlagiat()


##########################
# Go through each sentence, 
# check wether the sentence is present in each of it's search queries html code
# return a dictionary { String sentence; double plagiatPercentage}
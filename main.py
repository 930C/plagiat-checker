#!/usr/bin/env python3
from google import search
import urllib.request as urllib
import re
from bs4 import BeautifulSoup

#############
# Open File 

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
# Start google search
for j in search("Moderne Programmierkonzepe", tld="com", num=10, stop=10, pause=2):
    print(j)

##########################
# Open Link and read html
    site = urllib.urlopen(j)
    sitebytes = site.read()
    html = sitebytes.decode("utf8")
    site.close()
    clean_html = re.sub("<.*?>", " ", html)
    clean_html = re.sub(r"\s+", " ", clean_html)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n")
    print(clean_html)

import re

def checkPlagiat(sentence, pageContent, url):
    if sentence.upper() in pageContent.upper():
        return [sentence, url]
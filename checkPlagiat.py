import re

def checkPlagiat(sentence, html, url):
    sentenceUp = sentence.upper()
    sentenceRegex = "^" + sentenceUp + "$"
    htmlUp = html.upper()
    
    find = re.findall(sentenceRegex, htmlUp)
    if htmlUp.find(sentenceUp):
        return [sentence, url]
    
import re

def checkPlagiat(sentence, html, url):

    sentenceUp = sentence.upper()
    sentenceRegex = "^" + sentenceUp + "$"
    htmlUp = html.upper()
    
    find = re.findall(sentenceRegex, htmlUp)
    if list.__sizeof__(find) > 0:
        return "----------------\nPLAGIAT GEFUNDEN:\n " + sentence + "\n\nVon:\n" + url + "\n----------"
        # return true # TODO in regex verfeinerte Suche nach Plagiat (z.B. Kommatrennung)
    else:
        return None
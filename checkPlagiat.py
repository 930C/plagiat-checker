import re

def checkPlagiat(sentence, html, url):

    sentenceUp = sentence.upper()
    sentenceRegex = "^" + sentenceUp + "$"
    htmlUp = html.upper()
    
    find = re.findall(sentenceRegex, htmlUp)
    if list.__sizeof__(find) > 0:
        return "PLAGIAT GEFUNDEN: ----------------\n" + sentence + "\n-----\nVon:\t" + url
        # return true # TODO in regex verfeinerte Suche nach Plagiat (z.B. Kommatrennung)
    else:
        return None
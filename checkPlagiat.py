import re

def checkPlagiat(sentence, html, url):

    sentenceUp = sentence.upper()
    sentenceRegex = "^" + sentenceUp + "$"
    htmlUp = html.upper()
    


    find = re.findall(sentenceRegex, htmlUp)
    #if len(find) > 0:
    if htmlUp.find(sentenceUp):
        # return "----------------\nPLAGIAT GEFUNDEN:\n " + sentence + "\n\nVon:\n" + url + "\n----------"
        # return true # TODO in regex verfeinerte Suche nach Plagiat (z.B. Kommatrennung)
        print(len(find))
        return [sentence, url]
    
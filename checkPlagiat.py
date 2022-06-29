def checkPlagiat(sentence, html, url):

    sentenceUp = sentence.upper()
    htmlUp = html.upper()
    
    find = htmlUp.find(sentenceUp)
    if find > -1:
        return "Plagiat " + sentence + " an Stelle " + str(find) + " von " + url
        # return true # TODO in regex verfeinerte Suche nach Plagiat (z.B. Kommatrennung)
    else:
        return ""
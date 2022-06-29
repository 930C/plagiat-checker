def checkPlagiat(sentence, html):

    sentenceUp = sentence.upper()
    htmlUp = html.upper()

    print("SATZ " + sentence + "\n------------------\nHTML: " + html)
    
    find = htmlUp.find(sentenceUp)
    if find > -1:
        return "Plagiat " + sentence + " an Stelle " + str(find)
        # return true # TODO in regex verfeinerte Suche nach Plagiat (z.B. Kommatrennung)
    else:
        return "Der Satz " + sentence + "ist kein Plagiat."
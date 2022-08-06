import re

def cleaner(text, toDelete=["\n", "\xa0", "\t", ",", "↑"]):
    for i in toDelete : text = text.replace(i, " ") # Removes escape sequences
    text = re.sub("\[(.*?)\]", " ", text)           # Removes text between brackets (removes Wikipedia references)
    text = re.sub(" +", " ", text)                  # Removes multiple whitespaces
    return text

import re
import sentenceCleaner as sc

def splitter(text):
    text = sc.cleaner(text)     # clean text before split

    ausgabe = text.split(".")   # make a list and split between the periods

    for index, value in enumerate(ausgabe):
        if value.replace(" ", "") == "": ausgabe.pop(index)         # delete empty elements
        elif value[0] == " ": ausgabe[index] = value.lstrip(" ")    # delete leading whitespace

    return ausgabe

import re

def splitter(text):
    ausgabe = text.replace("\n", "").split(".")

    for index, value in enumerate(ausgabe):
        if value == "":
            ausgabe.pop(index)
        elif value[0] == " ":
            ausgabe[index] = value.lstrip(" ")
    return ausgabe

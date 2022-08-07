# Not in use
def readFile(file):
    try:
        f1 = open(file, "r",encoding='utf8')
        content = f1.read()
        f1.close()
        content = content.replace("\n", "").split(".")[0:-1]
        return content
    except BaseException as err:
        print(f"Fehler {err}")
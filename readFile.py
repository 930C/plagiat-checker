def readFile(file):
    try:
        f1 = open(file, "r")
        content = f1.read()
        f1.close()
        return content
    except BaseException as err1:
        print(f"Fehler {err1}")
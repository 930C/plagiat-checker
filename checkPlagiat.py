import re
from bs4 import BeautifulSoup
import urllib.request as urllib

def checkPlagiat(sentence, pageContent, url):

    sentenceUp = sentence.upper()
    # htmlUp = html.upper()

    # sourceCode = BeautifulSoup(html, "html.parser")
    # pageContent = sourceCode.text
    pageContentUp = pageContent.upper()
    
    if pageContentUp.find(sentenceUp):
        return [sentence, url]


if __name__ == "__main__": 
    print("testing")
    sentence = "In a similar fashion, Arch ships the configuration files provided by upstream with changes limited to distribution-specific issues like adjusting the system file paths."
    url = "https://wiki.archlinux.org/title/Arch_Linux"
    html = urllib.urlopen(url).read().decode("utf8")
    print(checkPlagiat(sentence, html, url))
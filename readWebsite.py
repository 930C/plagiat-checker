import urllib.request as urllib
# import re
from bs4 import BeautifulSoup
import sentenceCleaner as sc

def readWebsite(url):
    # site = urllib.urlopen(url)     
    # sitebytes = site.read()
    # html = sitebytes.decode("utf8")
    # site.close()
    # clean_html = re.sub("<.*?>", " ", html)
    # clean_html = re.sub("\s+", " ", clean_html)
    # return clean_html

    site = urllib.urlopen(url)
    siteDecoded = site.read().decode("utf8")
    site.close()

    page = BeautifulSoup(siteDecoded, "html.parser")
    pageContent = page.text
        
    cleanPageContent = sc.cleaner(pageContent)

    return cleanPageContent
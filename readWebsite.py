import urllib.request as urllib
import re

def readWebsite(url):
    site = urllib.urlopen(url)     
    sitebytes = site.read()
    html = sitebytes.decode("utf8")
    site.close()
    clean_html = re.sub("<.*?>", " ", html)
    clean_html = re.sub("\s+", " ", clean_html)
    return clean_html
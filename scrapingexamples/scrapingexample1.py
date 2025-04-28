import sys
import re
import shutil
import requests
from bs4 import BeautifulSoup as soup
# https://infatica.io/blog/web-crawling-vs-web-scraping/
def get_source(link):
    r = requests.get(link)
    if r.status_code == 200:
        page_content = soup(r.text,"html.parser")
        return page_content
    else:
        sys.exit()
        
def filter(html):
    imgs = html.findAll("img")
    if imgs:
        return imgs
    else:
        sys.exit()
    #print(imgs)

def main():
    html = get_source("http://books.toscrape.com/")
    images = filter(html)
    for image in images:
        src = image.get("src")
        #print(src)
        if src:
            name = src
            src = "http://books.toscrape.com/" + src
            print(src)
            r = requests.get(src,stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                f = open(name.split('/')[-1],"wb")
                shutil.copyfileobj(r.raw,f)
                f.close()
            

if __name__ == '__main__':
    main()

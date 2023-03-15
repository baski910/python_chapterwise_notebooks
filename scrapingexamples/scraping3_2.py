import requests
import sys
import shutil
import re
from bs4 import BeautifulSoup as soup

def get_source( link ):
    r = requests.get( link )
    if r.status_code == 200:
        page_content = soup( r.text ,'html.parser')
        return page_content
    else:
        sys.exit( "[~] Invalid Response Received." )

def filter( html ):
    imgs = html.findAll( "img" ) # <img src="" widhth
    if imgs:
        return imgs
    else:
        sys.exit("[~] No images detected on the page.")

def main():
    html = get_source( "https://www.drivespark.com/wallpapers/" )
    tags = filter( html )
    for tag in tags:
        src = tag.get( "src" )
        if src:
            src = re.match( r"((?:https?:\/\/.*)?\/(.*\.(?:png|jpg)))", src )
            if src:
                (link, name) = src.groups()
                if not link.startswith("http"):
                    link = "https://www.drivespark.com" + link
                print(link)

if __name__ == "__main__":
    main()

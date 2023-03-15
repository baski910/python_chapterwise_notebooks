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
    imgs = html.findAll( "img" )
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
                r = requests.get( link, stream=True )
                if r.status_code == 200:
                    r.raw.decode_content = True
                    f = open( name.split("/")[-1], "wb" )
                    shutil.copyfileobj(r.raw, f)
                    f.close()

if __name__ == "__main__":
    main()

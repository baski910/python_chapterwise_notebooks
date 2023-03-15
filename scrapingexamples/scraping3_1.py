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


def main():
    html = get_source( "https://www.drivespark.com/wallpapers/" )

if __name__ == "__main__":
    main()

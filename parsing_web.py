import requests
import csv
from lxml import etree
import lxml.html

url = 'https://habr.com/ru/post/220125/'

def parse(url):
    try:
        api = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    print(tree)
    text_original = tree.xpath('//*[@id="post-content-body"]/div/text()')
    for item in text_original:
        print(item)

def main():
    parse(url)

if __name__=="__main__":
    main()

import requests
from lxml import etree
import lxml.html
import csv

def parse(url):

    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/dev//*[@clas="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/dev//*[@clas="translate"]/text()')
    with open("text.ssv", newline='') as csv_file:
        write = csv.write(csv_file)
        for i in range(len(text_original)):
            write.writerow(text_original[i])
            write.writerow(text_translate[i])

def main():
    parse("https:/www.amalgama-lab.com/song/t/tone_and_i/dance_monkey.html")

if __name__ == "__main__":
    main()
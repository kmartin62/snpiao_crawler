from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

ford_path = "file:///C:/Users/Martin/Desktop/fords.html"
vw_path = "file:///C:/Users/Martin/Desktop/vw.html"
bmw_path = "file:///C:/Users/Martin/Desktop/bmw.html"

uClient = uReq(bmw_path)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

models = page_soup.findAll("span")[:-1]

for model in models:
    # print('-'.join(map(str, model.text.lower().split(" "))))
    # with open('ford_models.csv', 'a', newline='') as file:
    #     writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    #     writer.writerow(['-'.join(map(str, model.text.lower().split(" ")))])
    # with open('vw_models.csv', 'a', newline='') as file:
    #     writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    #     writer.writerow(['-'.join(map(str, model.text.lower().split(" ")))])
    with open('bmw_models.csv', 'a', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(['-'.join(map(str, model.text.lower().split(" ")))])

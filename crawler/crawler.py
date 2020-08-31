from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from crawler.constants import PAGE_URL, BMW_MODELS, CAR_DICT, AD_DICT, EQ_DICT, SELLER_DICT
from crawler.write_csv import write_to_csv
import time
import pandas as pd

SELLER_SET = set()
df = pd.read_csv("../sellers.csv")
saved_column = df.SellerID

for s in saved_column:
    SELLER_SET.add(s)


CURRENT_CAR = "bmw"
CAR_ID = 53946

for model in BMW_MODELS:
    for year in range(1991, 2021):
        tmp_year = year
        tmp_year_1 = year + 1
        for page in range(1, 21):
            URL = PAGE_URL + "/lst/{0}/{1}?sort=standard&desc=0&ustate=N%2CU&size=20&page={2}&fregto={3}&fregfrom={4}&atype=C&".format(
                CURRENT_CAR, model, page, tmp_year_1, tmp_year)
            try:
                uClient = uReq(URL)
                time.sleep(1)
                page_html = uClient.read()
                uClient.close()
            except:
                print("An error occured at {0}".format(URL))
                break

            page_soup = soup(page_html, "html.parser")

            containers = page_soup.findAll("div", {"class": "cl-list-element cl-list-element-gap"})
            if len(containers) == 0:
                break

            # break
            print(URL)
            for container in containers:
                TMP_CAR_DICT = CAR_DICT.copy()
                TMP_AD_DICT = AD_DICT.copy()
                TMP_EQ_DICT = EQ_DICT.copy()
                TMP_SELLER_DICT = SELLER_DICT.copy()

                # print(container.a["href"])
                time.sleep(1)
                try:
                    AD_URL = PAGE_URL + container.a["href"]
                except:
                    continue

                try:
                    uClient = uReq(AD_URL)
                    page_html = uClient.read()
                    uClient.close()
                except:
                    print("An error occured at {0}".format(AD_URL))
                    break

                ad_soup = soup(page_html, "html.parser")

                details = ad_soup.findAll("div", {"class": "cldt-item"})[1]
                tmp = ad_soup.findAll("as24-tracking")
                stage_data = ad_soup.findAll("div", {"class": "cldt-stage-data"})[0]

                PRICE = stage_data.findAll("div", {"class":"cldt-price"})[0].h2.text.strip().split(" ")[1].split(".")[0]

                TMP_CAR_DICT["Mileage"] = stage_data.findAll("span", {"class":"sc-font-l cldt-stage-primary-keyfact"})[0].text
                TMP_CAR_DICT["Power(hp)"] = stage_data.findAll("span", {"class":"sc-font-m cldt-stage-primary-keyfact"})[0].text
                TMP_CAR_DICT["Price"] = PRICE
                TMP_CAR_DICT["ID"] = CAR_ID

                for x, y in zip(details.findAll("dt"), details.findAll("dd")):
                    if x.text in TMP_CAR_DICT.keys():
                        TMP_CAR_DICT[x.text] = 1 if y.text.strip() == '' else y.text.strip()

                TMP_AD_DICT["AdID"] = [elem for elem in tmp if "classified_productID" in str(elem)][0]['as24-tracking-value'].split(":")[1][:-1].strip().split("\"")[1]
                TMP_AD_DICT["CarID"] = CAR_ID
                TMP_AD_DICT["SellerID"] = [elem for elem in tmp if "classified_customerID" in str(elem)][0]['as24-tracking-value'].split(":")[1][:-1].strip().split("\"")[1]
                TMP_AD_DICT["Title"] = ad_soup.find("h1", {"class" : "cldt-detail-title sc-ellipsis"}).text.strip()
                try:
                    TMP_AD_DICT["Description"] = ad_soup.find("div", {"data-type":"description"}).text.strip()
                except:
                    TMP_AD_DICT["Description"] = "NULL"

                TMP_AD_DICT["Price"] = PRICE
                TMP_AD_DICT["Type"] = details.findAll("a", {"class":"cldt-stealth-link"})[0].text
                TMP_AD_DICT["URL"] = container.a["href"]

                TMP_EQ_DICT["AdID"] = [elem for elem in tmp if "classified_productID" in str(elem)][0]['as24-tracking-value'].split(":")[1][:-1].strip().split("\"")[1]
                try:
                    equipment = ad_soup.find("div", {"data-item-name":"equipments"}).findAll("span")
                    for e in equipment:
                        if e.text in TMP_EQ_DICT.keys():
                            TMP_EQ_DICT[e.text] = 1
                except:
                    TMP_EQ_DICT = EQ_DICT.copy()

                try:
                    try:
                        vendor = stage_data.find("h3", {"data-item-name":"vendor-company-name"}).text
                    except:
                        vendor = stage_data.find("h3", {"data-item-name": "vendor-private-seller-title"}).text
                except:
                    continue

                city = ' '.join(map(str, stage_data.findAll("div", {"data-item-name":"vendor-contact-city"})[0].text.split(" ")[1:]))
                zip_code = stage_data.findAll("div", {"data-item-name":"vendor-contact-city"})[0].text.split(" ")[0]
                try:
                    country = stage_data.findAll("div", {"data-item-name": "vendor-contact-country"})[0].text
                except:
                    country = "NULL"

                TMP_SELLER_DICT["SellerID"] = [elem for elem in tmp if "classified_customerID" in str(elem)][0]['as24-tracking-value'].split(":")[1][:-1].strip().split("\"")[1]
                TMP_SELLER_DICT["Vendor"] = vendor
                TMP_SELLER_DICT["City"] = city
                TMP_SELLER_DICT["ZipCode"] = zip_code
                TMP_SELLER_DICT["Country"] = country

                SELLER_ID = [elem for elem in tmp if "classified_customerID" in str(elem)][0]['as24-tracking-value'].split(":")[1][:-1].strip().split("\"")[1]
                if SELLER_ID in SELLER_SET:
                    write_to_csv(TMP_CAR_DICT, TMP_AD_DICT, TMP_SELLER_DICT, TMP_EQ_DICT, 1)
                else:
                    SELLER_SET.add(SELLER_ID)
                    write_to_csv(TMP_CAR_DICT, TMP_AD_DICT, TMP_SELLER_DICT, TMP_EQ_DICT, 0)
                CAR_ID += 1

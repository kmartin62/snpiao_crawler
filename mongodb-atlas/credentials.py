from pymongo import MongoClient
import pandas as pd
import csv

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

# client = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.akjeu.mongodb.net/test_db?retryWrites=true&w=majority")

df = pd.read_csv("ads123_mod.csv")
# df1 = pd.read_csv("equipments_mod.csv")

lista = list()

tmp_dict = df.to_dict('records')
# eq_dict = df1.to_dict('records')

for elem in tmp_dict:
        try:
                d = pd.DataFrame([elem]).dropna(axis=1, how="all").to_dict('records')[0]
                if '\r\n' in d['Title']:
                    d['Title'] = d['Title'].replace('\r\n', ' ')
                elif '\n' in d['Title']:
                    d['Title'] = d['Title'].replace('\n', ' ')

                d['Price'] = int(d['Price'].replace(',', ''))
                # print(d['Price'])
                print(d)
                # print("-----------------------------------------------------------------------")
                lista.append(d)
        except:
                continue

client.cars_database.ads.insert_many(lista)
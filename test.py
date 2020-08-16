import pandas as pd

df = pd.read_csv("sellers.csv")
saved_column = df.SellerID

for s in saved_column:
    print(s)

# from constants import CAR_METRICS, AD_METRICS, SELLER_METRICS, EQ_METRICS
# import csv
#
# with open('cars.csv', 'w', newline='') as a, open('ads.csv', 'a', newline='') as c, open('sellers.csv', 'a', newline='') as s, open('equipment.csv', 'a', newline='') as e:
#     writer1 = csv.writer(a, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
#     writer2 = csv.writer(c, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
#     writer3 = csv.writer(s, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
#     writer4 = csv.writer(e, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
#
#     writer1.writerow(CAR_METRICS)
#     # writer2.writerow(AD_METRICS)
#     # writer3.writerow(SELLER_METRICS)
#     # writer4.writerow(EQ_METRICS)
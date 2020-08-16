import csv
from constants import CAR_METRICS, AD_METRICS, SELLER_METRICS, EQ_METRICS


def write_to_csv(car_dict, ads_dict, sellers_dict, eq_dict, flag):

    with open('cars.csv', 'a', newline='', encoding='utf-8') as a, open('ads.csv', 'a', newline='', encoding='utf-8') as c, open('sellers.csv', 'a', newline='', encoding='utf-8') as s, open('equipment.csv', 'a', newline='', encoding='utf-8') as e:
        writer1 = csv.writer(a, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer2 = csv.writer(c, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer3 = csv.writer(s, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer4 = csv.writer(e, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')

        # writer1.writerow(CAR_METRICS)
        # writer2.writerow(AD_METRICS)
        # writer3.writerow(SELLER_METRICS)
        # writer4.writerow(EQ_METRICS)
        if flag == 0:
            writer1.writerow(list(car_dict.values()))
            writer2.writerow(list(ads_dict.values()))
            writer3.writerow(list(sellers_dict.values()))
            writer4.writerow(list(eq_dict.values()))
        else:
            writer1.writerow(list(car_dict.values()))
            writer2.writerow(list(ads_dict.values()))
            writer4.writerow(list(eq_dict.values()))




import pandas as pd
#
# df = pd.read_csv('test.csv')
# dd = df.drop('ID', axis=1)
# dd.to_csv('test_1.csv', index=False)
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

df = pd.read_csv('../ads.csv')
dd = df.drop('CarID', axis=1)
# dd = df.drop('CarID', axis=1)
dd.to_csv('ads123_mod.csv', index=False)





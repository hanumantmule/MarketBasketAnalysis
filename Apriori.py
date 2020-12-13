import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# we need to install mlxtend on anaconda prompt by typing 'pip install mlxtend'
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

store_data = pd.read_csv('BreadBasket_DMS.csv', encoding="ISO-8859-1")

# lets visualize which items are more popular.

Items = {}
for item in store_data['Item']:
    if item in Items:
        Items[item] = Items[item] + 1
    else:
        Items[item] = 1

keys = []
vals = []
for i, k in Items.items():
    if k > 30:
        keys.append(i)
        vals.append(k)
plt.bar(keys, vals, label="Items sold in 2017")
plt.rcParams["figure.figsize"] = [20, 10]
plt.ylabel('Number of Transactions in Percentage')
plt.xlabel('Items Sold')
plt.xticks(list(keys), rotation=90)
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=0.)

# plt.show()


store_data['Quantity'] = 1

print(store_data.head(7))

basket = store_data.groupby(['Transaction', 'Item'])['Quantity'].sum().unstack().fillna(0)
print(basket.head())


# There are a lot of zeros in the data but we also need to make sure any positive values are converted to a 1
# and anything less the 0 is set to 0. This step will complete the one hot encoding of the data

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


basket_sets = basket.applymap(encode_units)
print(basket_sets.head())
frequent_itemsets = apriori(basket_sets,min_support=0.003,  use_colnames=True)
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules.head())


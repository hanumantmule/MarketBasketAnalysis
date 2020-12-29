import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# we need to install mlxtend on anaconda prompt by typing 'pip install mlxtend'
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from helper_functions import top_x_per_products, plot_graph


def start_apriori(top_percentage):
    store_data = pd.read_csv('../Datasets/BreadBasket.csv')
    # lets visualize which items are more popular.
    Items = {}
    for item in store_data['Item']:
        if item in Items:
            Items[item] = Items[item] + 1
        else:
            Items[item] = 1

    print(Items)
    top_items = top_x_per_products(Items,top_percentage)
    print(top_items)
    top_item_set = set(top_items.keys())
    print(top_item_set)

    plot_graph(top_items)

    store_data['D'] = store_data.Item.isin(top_item_set).astype(int)
    store_data['D'].apply(lambda x: 1 if x in top_item_set else 0)

    store_data = store_data[store_data['D'] == 1]
    print(store_data)

    store_data['Quantity'] = 1

    # print(store_data.head(7))

    basket = store_data.groupby(['Transaction', 'Item'])['Quantity'].sum().unstack().fillna(0)

    # There are a lot of zeros in the data but we also need to make sure any positive values are converted to a 1
    # and anything less the 0 is set to 0. This step will complete the one hot encoding of the data

    def encode_units(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1

    basket_sets = basket.applymap(encode_units)
    print(basket_sets.head())
    frequent_itemsets = apriori(basket_sets, min_support=0.01, use_colnames=True)
    print(frequent_itemsets)

    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
    print(rules)

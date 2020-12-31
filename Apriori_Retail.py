import collections, functools, operator
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

from helper_functions import top_x_per_products, plot_graph


def apriori_retail_dataset(TOP_PERCENTAGE):
    store_data = pd.read_csv('../Datasets/Market_Basket_Optimisation.csv', header=None)

    records = []
    for i in range(0, 7501):
        records.append([str(store_data.values[i, j]) for j in range(0, 20)])

    Items = dict(collections.Counter([x for sublist in records for x in sublist]))
    del Items['nan']
    print("Frequencies of Each Item:")
    print(Items)

    top_items = top_x_per_products(Items, TOP_PERCENTAGE)
    print("Top Items:")
    print(top_items)

    plot_graph(top_items,'apriori',TOP_PERCENTAGE)

    Output = [b for b in records if
              any(a in b for a in top_items.keys())]

    association_rules = apriori(Output, min_support=0.01, min_confidence=0.5, min_lift=2, min_length=1)
    association_results = list(association_rules)

    # print(association_results)
    print("\n=============== ASOCIATION RULES ======================")

    for item in association_results:
        # first index of the inner list
        # Contains base item and add item
        if 'nan' not in list(item[2][0][0]) and 'nan' not in list(item[2][0][1]):
            print("Rule: " + str(list(item[2][0][0])) + " -> " + str(list(item[2][0][1])))
            # second index of the inner list
            print("Support: " + str(item[1]))

            # third index of the list located at 0th
            # of the third index of the inner list

            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")

# Data manipulation libraries
import collections

import matplotlib as matplotlib
import pandas as pd
import numpy as np

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

from helper_functions import plot_graph, top_x_per_products

sns.set_style("dark")
import squarify
import matplotlib
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

# for preprocessing
from mlxtend.preprocessing import TransactionEncoder
# to print all the interactive output without resorting to print, not only the last result.
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
# for preprocessing
from mlxtend.preprocessing import TransactionEncoder


def fp_growth_retail(TOP_PERCENTAGE):
    data = pd.read_csv("../Datasets/Market_Basket_Optimisation.csv", header=None)

    # converting into required format of TransactionEncoder()
    trans = []
    for i in range(0, 7501):
        trans.append([str(data.values[i, j]) for j in range(0, 20)])

    Items = dict(collections.Counter([x for sublist in trans for x in sublist]))
    Items['nan']=0
    print("Frequencies of Each Item:")
    print(Items)

    top_items = top_x_per_products(Items, TOP_PERCENTAGE)
    print("Top Items:")
    print(top_items)

    plot_graph(top_items,'fp_growth',TOP_PERCENTAGE)

    Output = [b for b in trans if
              any(a in b for a in top_items.keys())]

    # Using TransactionEncoder
    trans = np.array(trans)

    Output = np.array(Output)
    # print(Output.shape)

    t = TransactionEncoder()
    data = t.fit_transform(Output)
    data = pd.DataFrame(data, columns=t.columns_, dtype=int)

    # print(data.shape)
    # here we also find nan as one of the columns so lets drop that column

    data.drop('nan', axis=1, inplace=True)
    # print(data.shape)
    # print(data.head())

    # running the fpgrowth algorithm
    res = fpgrowth(data, min_support=0.01, use_colnames=True)
    res = association_rules(res, metric="confidence", min_threshold=0.5)
    print("\n=============== ASOCIATION RULES ======================")
    print(res)

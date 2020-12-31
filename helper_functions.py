from itertools import chain

import matplotlib.pyplot as plt
import math


def top_x_per_products(products, percentage):
    val = math.ceil((len(products) * percentage) / 100)
    print(str(percentage) + ' Percentage of ' + str(len(products)) + ' is = ' + str(val))
    top_items = dict(sorted(products.items(), key=lambda item: item[1], reverse=True)[:val])
    return top_items


def plot_graph(Items,algorithm,top_per):
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
    # plt.savefig("../Graphs/"+algorithm+str(top_per)+".png")
    # plt.show()
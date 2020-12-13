import pandas as pd
import numpy as np
import pyfpgrowth
import sklearn

df = pd.read_csv("BreadBasket_DMS.csv", encoding="ISO-8859-1")

# imputer = sklearn.Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# imputer = imputer.fit(product[:, 1:2])
# product[:, 1:2] = imputer.transform(product[:, 1:2])

dictionary = {}
for group in np.unique(df.Transaction):
    df_group = df[df.Transaction == group]
    grouplist = np.unique(df_group.Item).tolist()
    print("group num : ", group, " :", grouplist)
    dictionary[group] = grouplist

patterns = pyfpgrowth.find_frequent_patterns(dictionary.values(), 2)

rules = pyfpgrowth.generate_association_rules(patterns, 0.03)

print(rules)

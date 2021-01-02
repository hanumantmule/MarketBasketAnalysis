from Apriori_BMS import start_apriori
from Apriori_Retail import apriori_retail_dataset
from fp_growth_Retail import fp_growth_retail
import time

top_percentage=[100, 55]

# start = (time.time() * 1000)

for p in top_percentage:
    print("\n\n ---- Running for top "+ str(p)+" percent Items --------- ")
    # fp_growth_retail(p,'Market_Basket_Optimisation',7501)
    apriori_retail_dataset(p)

# print(f'Time: {time.time()*1000 - start}')

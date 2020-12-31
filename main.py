from Apriori_BMS import start_apriori
from Apriori_Retail import apriori_retail_dataset
from fp_growth_Retail import fp_growth_retail

top_percentage = [40, 45, 50, 55, 60, 80, 100]
# start_apriori(55)

apriori_retail_dataset(40)


# Choose Top 30 40 50 55 80
# for percentage in top_percentage:
#     print("\n\n\n ---- Running for top "+ str(percentage)+" percent Items --------- ")
#     fp_growth_retail(percentage)

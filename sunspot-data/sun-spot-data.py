# A program that manipulates JSON Data on yearly averages of Wolf Sun Spot Data for years 1770-1869,
#  also known as Box-Jenkins Series E.

import json

with open('Sample-Data-Wolf-Sunspot-Numbers.json') as JsonObj:    # Creating File  Object.
    JsonData = json.load(JsonObj) # load(FileObj) to load File Object.

raw_list = []   # Defining  a list where the raw data from JSON File will be stored.
for list in JsonData:
    raw_list.append(list)   # JSON elements are appended to the empty list.

data_list = raw_list[2][1][1]    # The refined data is now moved to a new list.
data_list.remove("List" )    # The first element - "List" is removed.
print(data_list)

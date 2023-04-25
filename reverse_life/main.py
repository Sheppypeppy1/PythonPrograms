# importing the pandas library
import pandas as pd
import math

URL = "/Users/mitchelshephard/Desktop/reverselife/product-costs-2023-04-24-original.csv"
TARGET_URL = "/Users/mitchelshephard/Desktop/reverselife/product-costs-2023-04-24-modified.csv"

prices= {
    "FM":0.63,
    "UEM":0.35,
    "ES":2.6,
    "SM":1,
    "4NF":0.72,
    "DC":3.5,
    "NC":3.5,
    "MS":0.53,
    "BO":7.48,
    "MSM":5.75
}

codes = []

#Calculates the lifetime product cost based on the SKU combinations and relative prices for them as shown above
def calculate_LPC():
    boo = False
    for index, row in df.iterrows():
        if df.loc[index,"Lifetimely Product Cost"] > 0:
            continue
        raw_input = row["SKU"]
        clean_input = raw_input.split("+")
        for i in range(len(clean_input)):
            #removes spaces from either side of each item in clean_input
            clean_input[i] = clean_input[i].strip()
            #adds a 1 to items that dont have numerical start value
            if not clean_input[i][0].isnumeric():
                clean_input[i] = "1" + clean_input[i]
            #if input is not in the reference table, put LPC as "not found"
            if clean_input[i][1:] not in prices:
                #add code to codes
                codes.append(clean_input[i][1:])
                df.loc[index,"Lifetimely Product Cost"] = f"not found: {clean_input[i][1:]}"
            #if its in prices, and previous items in the SKU for this row were also in the prices column, ie. all values are accounted for:
            if (clean_input[i][1:] in prices) and (type(df.loc[index,"Lifetimely Product Cost"]) == float):
                if math.isnan(df.loc[index,"Lifetimely Product Cost"]):
                    df.loc[index,"Lifetimely Product Cost"] = float(0)
                df.loc[index,"Lifetimely Product Cost"] += round(int(clean_input[i][0]) * prices[clean_input[i][1:]],2)
                df.loc[index,"Lifetimely Product Cost"] = round(df.loc[index,"Lifetimely Product Cost"],2)

# reading the csv file
df = pd.read_csv(URL)

calculate_LPC()

df.to_csv(TARGET_URL,index=False)

#take set to remove duplicates
codes = set(codes)
print(codes)
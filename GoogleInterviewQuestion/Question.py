#function ConvertCurrency([conversion_rates],start_currency, end_currency)
#[conversion_rates]=[start, end, rate]
#e.g. convert_currency ([["USD","JPY",110],["USD","AUD",1.45],["JPY","GBP",0.0070]], "GBP", "AUD")

#First we know that if ["X","Y",Z] then the reverse is true ["Y","X",1/Z]

conversion_rates = [["USD","JPY",110],["USD","AUD",1.45],["JPY","GBP",0.0070],["USD","GBP",0.8]]

#Generates the full list of conversion rates by using complement of the original and concatenating
def generate_conversion_rates():
    convertion_rates_complement = [[item[1],item[0],1/item[2]] for item in conversion_rates]
    rates = conversion_rates + convertion_rates_complement
    return rates

#Generates start list of outcomes
def generate_start_list(full_conversion_rates, start_currency, end_currency):
    start_list = [item for item in full_conversion_rates if (item[0]==start_currency)]
    print(f"Start List: {start_list}")
    return start_list 


#Generates full list of outcomes
def generate_full_list(full_conversion_rates, start_currency, end_currency, start_list):
    for item in start_list:
        lead_currency = item[1]
        current_list = [[item]+[i] for i in full_conversion_rates if (i[0]==lead_currency and i[1]!=start_currency)]

    #recursive_part = generate_full_list(full_conversion_rates, start_currency, end_currency, current_list)
    
    return current_list

def convert_currency(conversion_rates, start_currency, end_currency):
    full_conversion_rates = generate_conversion_rates()
    start_list = generate_start_list(full_conversion_rates, start_currency, end_currency)
    full_list = generate_full_list(full_conversion_rates, start_currency, end_currency, start_list)
    print(f"Full List: {full_list}")
    

convert_currency(conversion_rates, "GBP", "USD")
#with open("weather_data.csv") as file:
#    contents = file.readlines()
#
#print(contents)

#import csv 
#
#with open("weather_data.csv") as file:
#    contents = csv.reader(file)
#    temperatures = []
#    for row in contents:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#        print(row)
#    print(temperatures)

#import pandas
#
#data = pandas.read_csv("weather_data.csv")
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(temp_list)
#
#average = sum(temp_list)/len(temp_list)
#print(average)
#
#print(data[data.day == "Monday"])

#Create a pandas DF that contains 2 columns: Primary Fur Color, Count of those colors

import pandas 

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
pd_data = pandas.DataFrame(new_data)
pd_data.to_csv("Squirrel_Color_Counts.csv")
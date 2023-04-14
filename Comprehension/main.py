#import random
#
#names = ["Mitch","Alex","John","Freddie","Jade","Isabel"]
#
#students_scores = {item:random.randint(1,100) for item in names}
#print(students_scores)
#
#passed_students = {name:score for (name,score) in students_scores.items() if score >= 60}
#print(passed_students)
#
#sentence = "Hello my name is Mitch and I like to do programming for fun!"
#
#words = sentence.split()
#
#word_dict = {word:len(word) for word in words}
#print(word_dict)

#temperatures = {
#    "Monday" : 12,
#    "Tuesday" : 14,
#    "Wednesday" : 54,
#    "Thursday" : 43,
#    "Friday" : 32
#}
#
#def celcius_to_f(celcius):
#    return ((celcius * (9/5)) + 32)
#
#temperatures_f = {day:celcius_to_f(celcius) for (day,celcius) in temperatures.items()}
#
#print(temperatures_f)

import pandas as pd 

temperatures = {
    "Days" : ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "Temperatures" : [21,24,45,56,34]
}

temperatures_df = pd.DataFrame(temperatures)

for (key,value) in temperatures_df.items():
    print(value)

#iterrows is inbuilt loop in pandas that allows looping over rows..

for (index, row) in temperatures_df.iterrows():
    print(row.Temperatures)

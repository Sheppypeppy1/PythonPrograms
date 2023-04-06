import random

names = input("Please enter a list of you and your friends names, seperated by a comma:")
list_of_names = names.split(",")
print(list_of_names)

random_int = random.randint(0,len(list_of_names)-1)

print(f"The number picker chose person {random_int}, which means that {list_of_names[random_int]} is paying the bill!")

#another version of this program is to use random.choice where you pass the items that you want to randomly choose from:

person = random.choice(list_of_names)
print(f"The person who pays the bill is {person}")
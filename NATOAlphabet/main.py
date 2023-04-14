

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas 

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter:row.code for (index,row) in data.iterrows() if row.letter!="letter"}
print(NATO_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word to be spelt phonetically: ")
NATO_input = [NATO_dict[character.upper()] for character in user_input]
print(NATO_input)

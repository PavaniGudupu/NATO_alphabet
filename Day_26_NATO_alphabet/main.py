import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
df = {row.letter : row.code for (index, row) in data.iterrows()}

word = input("Enter your name: ").upper()
output_list = [df[letter] for letter in word]
print(output_list)
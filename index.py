import json

#open file in read mode
f = open('resources/dictionary.json')
#reading json data in dictionary format
dictionary = json.load(f)
print(dictionary['mixer'])
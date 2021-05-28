import json

#open file in read mode
f = open('resources/dictionary.json')
#reading json data in dictionary format
dictionary = json.load(f)
#get input
word = input("please enter the word : ")
word = word.lower()  
#checking if the word exists
if word in dictionary.keys():
    print(dictionary[word])
else:
    print('The word does not exist')    
    
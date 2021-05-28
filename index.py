import json,difflib

f = open('resources/data.json')
dictionary = json.load(f)
word = input("please enter the word : ")
word = word.lower()  

def checkSimilarity(word):
    wordlist = []
    for key in dictionary:
        wordlist.append(key)
    similar_words = difflib.get_close_matches(word,wordlist)
    i=1
    for similar_word in similar_words:
        print(f'{i}. {similar_word}')
        i=i+1

#checking if the word exists
if word in dictionary.keys():
    print('---------------')
    print(dictionary[word])
else:
    print('The word does not exist. Did you mean any of the following')    
    #check similarities
    checkSimilarity(word)
f.close()    
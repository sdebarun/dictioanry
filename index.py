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
    return similar_words
    
# def closeMatchInput(serial,words):

if word in dictionary.keys():
    print('---------------')
    print(dictionary[word])
else:
    print('The word does not exist.')    
    close_match = checkSimilarity(word)
    if len(close_match) > 0:
        print('Did you mean any of these (type the serial or no) : ')
        i=1
        for similar_word in close_match:
            print(f'{i}. {similar_word}')
            i=i+1
    closeword_serial = input()
    if closeword_serial != 'no':
        print(dictionary[close_match[int(closeword_serial)-1]])
    # closeword_serial = 'string'

    # while not closeword_serial.isdigit():
    #     print(">>>", end="")
    #     closeword_serial = input()
    #     if not closeword_serial.isdigit():
    #         print('Please enter the associated serial number from the above list')
    
f.close()    
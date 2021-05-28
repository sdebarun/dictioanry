import json,difflib

f = open('resources/data.json')
dictionary = json.load(f)
word = input("please enter the word : ")
word = word.lower()  

def checkSimilarity(word):
    """Founding the close matching words of a word 

    Args:
        word (string): Word for which close mnatches to be found

    Returns:
        list: a list of close matchig words
    """
    wordlist = []
    for key in dictionary:
        wordlist.append(key)
    similar_words = difflib.get_close_matches(word,wordlist)
    return similar_words
    

def renderDefinition(word):
    """This is function to show the definition of the word

    Args:
        word (string): The word whole definition needs to be looked upon
    """
    if len(dictionary[word]) > 1:
        count = 1
        for definition in dictionary[word]:
            print(f'{count}. {definition}')
            count = count+1
    else:
        print(dictionary[word][0]) 
       
if word in dictionary.keys():
    print('---------------')
    renderDefinition(word)
else:
    print('The word does not exist.')    
    closematches = checkSimilarity(word)
    if len(closematches) > 0:
        print('Did you mean any of these (enter the the serial or no) : ')
        i=1
        for similar_word in closematches:
            print(f'{i}. {similar_word}')
            i=i+1
    closeword_serial = input()
    if closeword_serial != 'no':
        index = int(closeword_serial)-1
        chosen_word = closematches[index]
        renderDefinition(chosen_word)
    # closeword_serial = 'string'

    # while not closeword_serial.isdigit():
    #     print(">>>", end="")
    #     closeword_serial = input()
    #     if not closeword_serial.isdigit():
    #         print('Please enter the associated serial number from the above list')
    
f.close()    
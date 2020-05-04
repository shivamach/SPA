import json
#imports


def setup(filename):
    global data
    data = json.load(open(filename))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        print("word does not exist in database")
        return 0

def printdef(output):
    '''this function sees the no of items in the list and prints them as numerical bulleted points'''
    for (i,item) in enumerate(output):
        print(f"{i} {item}")
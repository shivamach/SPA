import json


# imports


def setup(filename):
    global data
    data = json.load(open(filename))
    global keys
    keys = data.key()


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("word does not exist in database")
        return 0


def printdef(output):
    '''this function sees the no of items in the list and prints them as numerical bulleted points'''
    for (i, item) in enumerate(output):
        print(f"{i} {item}")

import json
from difflib import get_close_matches

data = json.load(open("original.json"))
keys = data.keys()

print("Press q to quit")
while(True):
    print("Enter the word: ")
    word = input()
    if word == 'q':
        print("closing....")
        break
    close_list = get_close_matches(word, keys)
    word = close_list[0]
    if len(close_list)==0:
        print("No such word found")
    elif word in data:
        for (i,item) in enumerate(data[word]):
            print(f"{i} {item}")







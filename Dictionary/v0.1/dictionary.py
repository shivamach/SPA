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
    if word in data:
        result = data[word]
    elif word.upper() in data:
        result = data[word.upper()]
    elif word.title() in data:
        result = data[word.title()]
    elif len(close_list)>0:
        print("Did you mean any of these words- ")
        for (i,item) in enumerate(close_list):
            print(f"{i} - {item}")
        print("Enter n if none of the words matched, or their index if they do")
        inp = input()
        if inp == 'n':
            print("re-enter the word")
            continue
        else:
            inp = int(inp)
            result = data[close_list[inp]]
    else:
        result = 000

    if result == 000:
        print("no such word found")
    else:
        for (i,item) in enumerate(result):
            print(f"{i}- {item}")










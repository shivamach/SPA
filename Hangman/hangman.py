def print_hangman(chances):
    # prints the hangman based on number of chances left
    if chances==8:
        print("---------")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("---------")
    elif chances==7:
        print("---------")
        print("         ")
        print("    0    ")
        print("         ")
        print("         ")
        print("         ")
        print("---------")
    elif chances == 6:
        print("---------")
        print("         ")
        print("    0    ")
        print("    |    ")
        print("         ")
        print("         ")
        print("---------")
    elif chances == 5:
        print("---------")
        print("         ")
        print("    0    ")
        print("    |    ")
        print("   /     ")
        print("         ")
        print("---------")
    elif chances == 4:
        print("---------")
        print("         ")
        print("    0    ")
        print("    |    ")
        print("   / \   ")
        print("         ")
        print("---------")
    elif chances == 3:
        print("---------")
        print("         ")
        print("    0    ")
        print("  / |    ")
        print("   / \   ")
        print("         ")
        print("---------")
    elif chances == 2:
        print("---------")
        print("         ")
        print("    0    ")
        print("  / | \  ")
        print("   / \   ")
        print("         ")
        print("---------")
    elif chances == 1:
        print("---------")
        print("         ")
        print("  L 0    ")
        print("  / | \  ")
        print("   / \   ")
        print("         ")
        print("---------")
    else:
        print("---------")
        print("  O-O-O  ")
        print("  L 0    ")
        print("  / | \  ")
        print("   / \   ")
        print("         ")
        print("---------")
        print("Hanged Man!!")

def guess(word_list,guess_list,chances):
    print("Enter your guess-")
    guess = input()
    loop = range(len(word_list))

    if guess in word_list:
        # update guess list and print guess list
        for i in loop:
            if word_list[i] == guess:
                guess_list[i] = guess
        for i in loop:
            print(guess_list[i], end="")
        print(".")
        print(f"{chances} are left")
        print_hangman(chances)
        return(word_list,guess_list,chances)
    else:
        print(f"{guess} is not present in the word, wrong guess")
        for i in loop:
            print(guess_list[i],end="")
        print(".")
        chances = chances - 1
        print(f"{chances} left")

        print_hangman(chances)
        return(word_list,guess_list,chances)








if __name__ == "__main__":
    print("**********************  Welcome to Hangman  ******************************")
    print("press ctrl+c to quit")


    while(True):
        word_list = []
        guess_list = []
        chances = 8
        # number of chances left
        print("Enter the word to be guessed")
        word = input()
        word = word.lower()
        length = len(word)
        # word in lower case and put into the lists
        for i in range(length):
            print(" _",end="")
            word_list.append(word[i])
            guess_list.append("_ ")
        # guess_list is used for printing, and word_list for comparing
        print(".")
        # now the loop for guesses and all
        while(True):
            #this loop is for guessing until chances is not equal to zero
            if chances==0:
                if word_list == guess_list:
                    for i in range(len(guess_list)):
                        print(guess_list[i],end="")
                    print(".")
                    print(f"you guessed the word with {chances} guesses remaining")
                    break
                else:
                    for i in range(len(guess_list)):
                        print(guess_list[i],end="")
                    print(".")
                    print("Failed to guess the word")
                    print_hangman(0)
                    print("game lost")
                    break

            else:
                (word_list,guess_list,chances) = guess(word_list,guess_list,chances)
                if word_list == guess_list:
                    for i in range(len(guess_list)):
                        print(guess_list[i],end="")
                    print(".")
                    print(f"you guessed the word with {chances} guesses remaining")
                    break
        print("Enter q to quit, any other key to play again")
        inp = input()
        if inp == 'q':
            break
        else:
            continue







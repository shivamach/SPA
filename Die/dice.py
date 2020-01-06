

rollthedice()

def rollthedice():
    print("Enter Number of Dice = ")
    input(dice_no)
    dice_set = [1,2,3,4,5,6]
    i = 0

    while(i<dice_no):
        value = choice(dice_set)
        container(value)
        i = i + 1

    print("press 'y' to roll again")
    print("press any other key to exit")
    input(alpha)

    if alpha == 'y':
        rollthedice()
    else:
        return 0

def container(value):
#i wanted to make a decent independent code taking advantage of looping
# and everything but that seems pointless when a simple solution is available at hand
    if value == 1:
        print("===========")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print("===========")
    elif value == 2:
        print("===========")
        print("|         |")
        print("| o     o |")
        print("|         |")
        print("===========")
    elif value == 3:
        print("===========")
        print("|    o    |")
        print("|    o    |")
        print("|    o    |")
        print("===========")
    elif value == 4:
        print("===========")
        print("| o    o  |")
        print("|         |")
        print("| o    o  |")
        print("===========")
    elif value == 5:
        print("===========")
        print("| o    o  |")
        print("|    o    |")
        print("| o    o  |")
        print("===========")
    else:
        print("===========")
        print("|o   o   o|")
        print("|         |")
        print("|o   o   o|")
        print("===========")
#simple code no issues of all those layers and bullshit this works well

import main
# imports

main.setup("original.json")
search = input(":")
output = main.translate(search)
if output != 0:
    main.printdef(output)



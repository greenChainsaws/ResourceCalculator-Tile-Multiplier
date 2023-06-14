## Hello World
f = open("resources.txt", "r")
lines = f.readlines()
f.close()

multiplier = int(input("How many tiles would you like to make?\n"))
x = 0
while x < len(lines):
    printme = lines[x]
    try:
        printme = int(printme)
        printme *= multiplier
    except:
        pass
    print(printme)
    x += 1

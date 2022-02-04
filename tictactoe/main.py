import sys


def inputs(l1, line, column):
    if l1[line - 1][column - 1] == "x" or l1[line - 1][column - 1] == "o":
        print("spot not vacant retry another spot")
        line1 = int(input("line:"))
        column1 = int(input("column:"))

        inputs(l1, line1, column1)
    else:
        l1[line - 1][column - 1] = p1


def inputs2(l1, line, column):
    if l1[line - 1][column - 1] == "x" or l1[line - 1][column - 1] == "o":
        print("spot not vacant retry another spot")
        line1 = int(input("line:"))
        column1 = int(input("column:"))
        inputs2(l1, line1, column1)
    else:
        l1[line - 1][column - 1] = p2


def ttt(p1, p2):
    l1 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    counter = 0
    while True:
        line = int(input("line:"))
        column = int(input("column:"))
        if counter % 2 == 0:
            inputs(l1, line, column)
            counter += 1
        elif counter % 2 == 1:
            inputs2(l1, line, column)
            counter += 1
        for i in l1:
            print(*i, sep="|")
            print("-----")
            conditions(l1)


def conditions(l1):
    for i in range(0, 3):
        if l1[i][0] == l1[i][1] == l1[i][2] == "x" or l1[i][0] == l1[i][1] == l1[i][2] == "o":
            print(l1[i][0], "wins")
            sys.exit(0)
        elif l1[0][i] == l1[1][i] == l1[2][i] == "x" or l1[0][i] == l1[1][i] == l1[2][i] == "o":
            print(l1[0][i], "wins")
            sys.exit(0)
        elif l1[0][0] == l1[1][1] == l1[2][2] == "x" or l1[0][0] == l1[1][1] == l1[2][2] == "o":
            print(l1[0][0], "wins")
            sys.exit(0)
        elif l1[0][2] == l1[1][1] == l1[2][0] == "x" or l1[0][2] == l1[1][1] == l1[2][0] == "o":
            print(l1[0][2], "wins")
            sys.exit(0)
    count = 0
    for i in l1:
        for j in range(0, 3):
            if i[j] == "x" or i[j] == "o":
                count += 1
    if count == 9:
        print("tie")
        sys.exit(0)


choose = input("player 1 choose X or o:")
if choose == "x":
    p1 = "x"
    p2 = "o"
    ttt(p1, p2)

elif choose == "o":
    p1 = "o"
    p2 = "x"
    ttt(p1, p2)
else:
    print("invalid choice")


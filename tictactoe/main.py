import sys

def inputs(line, column, l1, l2, l3):
    if line == 1:
        if column == 1:
            l1[0] = p1
        elif column == 2:
            l1[1] = p1
        elif column == 3:
            l1[2] = p1
    elif line == 2:
        if column == 1:
            l2[0] = p1
        elif column == 2:
            l2[1] = p1
        elif column == 3:
            l2[2] = p1
    elif line == 3:
        if column == 1:
            l3[0] = p1
        elif column == 2:
            l3[1] = p1
        elif column == 3:
            l3[2] = p1


def inputs2(line, column, l1, l2, l3):
    if line == 1:
        if column == 1:
            l1[0] = p2
        elif column == 2:
            l1[1] = p2
        elif column == 3:
            l1[2] = p2
    elif line == 2:
        if column == 1:
            l2[0] = p2
        elif column == 2:
            l2[1] = p2
        elif column == 3:
            l2[2] = p2
    elif line == 3:
        if column == 1:
            l3[0] = p2
        elif column == 2:
            l3[1] = p2
        elif column == 3:
            l3[2] = p2


def conditions(l1, l2, l3):
    a = 1
    if l1[0] == l1[1] == l1[2] == "x" or l1[0] == l1[1] == l1[2] == "o":
        print(l1[0], "wins")
        sys.exit(0)
    elif l2[0] == l2[1] == l2[2] == "x" or l2[0] == l2[1] == l2[2] == "o":
        print(l2[0], "wins")
        sys.exit(0)
    elif l3[0] == l3[1] == l3[2] == "x" or l3[0] == l3[1] == l3[2] == "o":
        print(l3[0], "wins")
        sys.exit(0)
    elif a == 1:
        for j in range(0, 3):
            if l1[j] == l2[j] == l3[j] == "x" or l1[j] == l2[j] == l3[j] == "o":
                print(l1[j], "wins")
                sys.exit(0)
            else:
                continue

        if l1[0] == l2[1] == l3[2] == "x" or l1[2] == l2[1] == l3[0] == "o":
            print(l1[0], "wins")
            sys.exit(0)
        elif l1[2] == l2[1] == l3[0] == "x" or l1[2] == l2[1] == l3[0] == "o":
            print(l1[2], "wins")
            sys.exit(0)


def ttt(p1, p2):
    l1 = [" ", " ", " "]
    l2 = [" ", " ", " "]
    l3 = [" ", " ", " "]

    counter = 0
    while counter < 9:
        conditions(l1, l2, l3)
        line = int(input("Line:"))
        column = int(input("Column:"))

        if counter % 2 == 0:
            inputs(line, column, l1, l2, l3)
            counter += 1

        elif counter % 2 == 1:
            inputs2(line, column, l1, l2, l3)
            counter += 1

        print(*l1, sep="|")
        print("-|-|-")
        print(*l2, sep="|")
        print("-|-|-")
        print(*l3, sep="|")
    else:
        print("Tie")


choose = input("player 1 choose X or o:")
if choose == "x":
    p1 = "x"
    p2 = "o"
    ttt(p1, p2)

elif choose == "o":
    p1 = "o"
    p2 = "x"
    ttt(p1, p2)


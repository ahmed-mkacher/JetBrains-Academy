import math

verif = True
winner = []
one = True
game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
xz = game.count("X")
oz = game.count("O")


def grid():
    print("---------")
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(f"{game[i][j]} ", end="")
        print("|")
    print("---------")


grid()


def declare():
    row, column = map(str, input("Enter coordinates here: ").split())
    if not (row.isdecimal() and column.isdecimal()):
        print("You should enter numbers!")
    row = int(row)
    column = int(column)
    return (row, column)


def diagonal():
    global winner
    for i in range(2):
        if not game[i][i] == game[i + 1][i + 1] or game[i][i] == " ":
            return False
    winner.append(game[i][2 - i])
    return True


def o_diagonal():
    global winner
    for i in range(2, 0, -1):
        if not game[i][2 - i] == game[i - 1][2 - i + 1] or game[i][2 - i] == " ":
            return False
    winner.append(game[i][i])
    return True


def columns():
    global winner, one
    for i in range(3):
        one = True
        for j in range(2):
            if not game[i][j] == game[i][j + 1]:
                one = False
        if one and game[i][j] != " ":
            winner.append(game[i][j])
    return True


def rows():
    global winner, one
    for j in range(3):
        one = True
        for i in range(2):
            if not game[i][j] == game[i + 1][j]:
                one = False
        if one and game[i][j] != " ":
            winner.append(game[i][j])
    return True


def call():
    diagonal()
    rows()
    o_diagonal()
    columns()


def win():
    global winner, oz, xz
    if "O" in winner and "X" in winner or math.fabs(oz - xz) > 1:
        print("Impossible")
    elif (diagonal() or rows() or columns() or o_diagonal()) and len(winner) > 0:
        print(f"{winner[0]} wins")


for i in range(9):
    coords = declare()
    free = True
    while free:
        free = False
        while coords[0] > 3 or coords[0] < 0 or coords[1] > 3 or coords[1] < 0:
            free = True
            print("Coordinates should be from 1 to 3!")
            coords = declare()
            while game[coords[0] - 1][coords[1] - 1] != " ":
                free = True
                print("This cell is occupied! choose another one!")
                coords = declare()
    if game[coords[0] - 1][coords[1] - 1] == " " and i % 2 == 0:
        game[coords[0] - 1][coords[1] - 1] = "X"
    elif game[coords[0] - 1][coords[1] - 1] == " ":
        game[coords[0] - 1][coords[1] - 1] = "O"
    call()
    grid()
    win()

if len(winner) == 0:
    print("Draw")

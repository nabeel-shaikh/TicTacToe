board = []
spot = [""]
for x in range(3):
    board.append(spot * 3)

def move(player):
    choice = False
    while not choice:
        row = int(input("{} Please select a row: ".format(player)))
        col = int(input("{} Please select a column: ".format(player)))
        choice = checkchoice(row, col)
    board[row][col] = player

def checkchoice(row,col):
    if (row) <3 and (row)>=0 and (col)<3 and (col) >=0:
        return True
    return False

def checkgame():
    gamestatus = False
    winner = None
    #horizontal check
    for x in range(3):
        if board[x][0] ==board[x][1] == board[x][2] != "":
            winner = board[x][0]
            gamestatus= True

    #vertical check
    for x in range(3):
        if board[0][x] ==board[1][x] == board[2][x] != "":
            winner = board[0][x]
            gamestatus= True

    #diagonal check
    if board[0][0]==board[1][1] == board[2][2] != "":
        winner = board[0][0]
        gamestatus = True
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        gamestatus = True
    
    return gamestatus, winner
    
player1 = ""
while player1 == "":
    player1 = input("Player 1 please enter 'X' or 'O': ")
    if player1 == "X":
        player2 = "O"
    elif player1 == "O":
        player2 = "X"
    else:
        player1 = ""

print("Player 1: {}".format(player1))
print("Player 2: {}".format(player2))
for x in range(3):
    print(board[x])

gamestatus = False
while not gamestatus:
    move(player1)
    for x in range(3):
        print(board[x])
    gamestatus, winner = checkgame()
    if not gamestatus:
        move(player2)
        for x in range(3):
            print(board[x])
        gamestatus, winner = checkgame()
    if gamestatus:
        print("The game is over, {} won!".format(winner))
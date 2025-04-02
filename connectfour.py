p1token = "r"
p2token = "b"

global board
board = [["_"]*7 for i in range(6)]

global turn
turn = 0

def start_game():
    board = [["_"]*7 for i in range(6)]
    print_game()
    request_move()

def check_adjacent(x,y):
    token = board[x][y]

    for i in range(3):
        if board[x+i][y] != token:
            return False

    return True


def check_wins():
    global turn
    for i in range(5):
        for j in range(6):
            if board[i][j] != "_":
               if check_adjacent(i,j):
                   print("player "+str(turn)+" wins!")
    
    if turn == 1: turn == 0
    else: turn == 1


    request_move()

def request_move():

    global turn

    move = input()
    coords = move.split()
    if len(coords) != 2: 
        print("nvalid input. Must be two space seperated numbers.")
    try:
        int(coords[0])
        int(coords[1])
    except ValueError:
        print("Both values must be whole numbers.")
        request_move()
    
    x = int(coords[0])
    y = int(coords[1])

    if turn == 0:
        board[x][y] = p1token
        
        print_game()
    else:
        board[x][y] = p2token
        
        print_game()
    
    check_wins()
    




def print_game():
    for i in range(6):
        print(str(i)+":"+str(board[i]))
    
    print("____0____1____2____3____4____5____6")

    return board

start_game()
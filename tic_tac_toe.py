import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
player1=input("Hey Player 1, Please enter your name: ")
player2=input("Hey Player 2, Please enter your name: ")
p1s='X'
p2s='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            return True
    return False
    
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            return True
    return False
    
def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        return True        
    return False    

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter the row value among 1 or 2 or 3: "))
        col=int(input("Enter the col value among 1 or 2 or 3: "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid input, please input again")
    board[row-1][col-1]=symbol

def tictactoe():
    print("So, let's start the game: TicTacToe")
    for turn in range(9):
        if turn%2==0:
            print(" ")
            print("Hey",player1, "it's your turn with X")
            place(p1s)
            if won(p1s):
                print("Hey",player1,"you won")
                break
        else:
            print(" ")
            print("Hey", player2, "it's your turn with O")
            place(p2s)
            if won(p2s):
                print("Hey",player2,"you won")
                break
    if not(won(p1s)) and not(won(p2s)):
        print("You people have drawn the match")
        print(numpy.matrix(board))

tictactoe()
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')
    print('____________')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('____________')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

def isBoardFull(board): 
    return board.count(' ') < 1

def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove():
    run = True
    while run:
        move = input('Please select a position beteween 1 and 9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('You must type a number between 1 and 9')
        except:
            print('You must type a number')

def selectRandom(lst):
    import random
    ln = len(lst)
    r = random.randrange(0, ln)
    return lst[r]

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    # checks for winning moves for either computer or player
    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardcopy= board[:]
            boardcopy[i] = letter
            if isWinner(boardcopy, letter):
                move = i
                return move

    # checks for available corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # choose random corner value
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)

    # otherwise check and return mid value
    if 5 in possibleMoves:
        move = 5
        return move

    # checks for avialable edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    # choose randome edge value
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
    return move

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, you lost!")
            break
        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print("Tie game!")
                break
            else:
                insertLetter('O', move)
                print("Computer placed an o on position", move, ":")
                printBoard(board)
        else:
            print("Congrats, you win!")
            break

while True:
    x = input("Do you want to play a game? (y/n)   ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('_________________')
        main()
    else:
        break
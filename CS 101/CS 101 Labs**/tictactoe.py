board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def printboard():
    print(' ', '1' , ' ', '2', ' ', '3')
    print('1', board[0][0], '|', board[0][1], '|', board[0][2])
    print(' ', '-', '+', '-', '+', '-')
    print('2', board[1][0], '|', board[1][1], '|', board[1][2])
    print(' ', '-', '+', '-', '+', '-')
    print('3', board[2][0], '|', board[2][1], '|', board[2][2])
    
printboard()

def playermoves():
    user1_input = input('First player move(X Y): ').split()
    user1_input = [int(i) for i in user1_input]
    board[user1_input[1] - 1][user1_input[0] - 1] = 'X'
    printboard()
    user2_input = input('Second player move(X Y): ').split()
    user2_input = [int(i) for i in user2_input]
    board[user2_input[1] - 1][user2_input[0] - 1] = '0'
    printboard()

win = False
while win == False:
    if ((board == [['0', '0', '0'],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]) or
        (board == [[' ', ' ', ' '],
                 ['0', '0', '0'],
                 [' ', ' ', ' ']]) or
        (board == [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 ['0', '0', '0']]) or
        (board == [['0', ' ', ' '],
                 ['0', ' ', ' '],
                 ['0', ' ', ' ']]) or
        (board == [[' ', '0', ' '],
                 [' ', '0', ' '],
                 [' ', '0', ' ']]) or
        (board == [[' ', ' ', '0'],
                 [' ', ' ', '0'],
                 [' ', ' ', '0']]) or
        (board == [['0', ' ', ' '],
                 [' ', '0', ' '],
                 [' ', ' ', '0']]) or
        (board == [[' ', ' ', '0'],
                 [' ', '0', ' '],
                 ['0', ' ', ' ']])):
        print('Winner')
        win = True
    else:
        playermoves()


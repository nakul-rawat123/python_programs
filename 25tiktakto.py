def print_board(board):
    print(board['9']+'|'+board['8']+'|'+board['7'])
    print('-+-+-')
    print(board['6'] + '|' + board['5'] + '|' + board['4'])
    print('-+-+-')
    print(board['3'] + '|' + board['2'] + '|' + board['1'])
board = {
    '9' :' ','8':' ','7':' ',
    '6':' ','5':' ','4':' ',
    '3':' ','2':' ','1':' '
}
print_board(board)
turn = 'X'
count = 0
while True:
    print('its your turn:',turn)
    move = input('which place do you want to move: ')
    if board[move]==' ':
        board[move]=turn
        count=count+1
    else:
        print('the place is already filled, move to another place')
        continue
    if count>=5:
        if board['9']==board['8']==board['7']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['6']==board['5']==board['4']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['3']==board['2']==board['1']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['9']==board['6']==board['3']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['8']==board['5']==board['2']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['7']==board['4']==board['1']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['9']==board['5']==board['1']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
        elif board['7']==board['5']==board['3']!=' ':
            print_board(board)
            print('game over')
            print(turn,'has won')
            break
    if count==9:
        print('its a draw')
        break
    if turn=="X":
        turn='O'
    else:
        turn='X'
    print_board(board)
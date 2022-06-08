# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно 
#было в одиночку. 
board=['','','','','','','','','']

def print_state(state):
    for i, c in enumerate(state):
        if (i+1)%3==0:
            print(f'{c}|')
        else:
            print(f'{c}|', end= '')
print_state(board)
winning_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def get_winner(state, combinations):
    for (x,y,z) in combinations:
        if state[x]==state[y] and state [z] == state[x] and (state[x]=='X'or state[x]=='0'):
            return state [x]
    return ''

def play_game(board):
    current_sing ='X'
    while(get_winner(board, winning_combinations)==''):
        index= int (input(f'Где хочешь нарисовать {current_sing} ?'))
        board[index]= current_sing
        
        print_state(board)

        winner_sing = get_winner(board, winning_combinations)
        if winner_sing != '':
            print(f'Вы выиграли! :{winner_sing}')

        current_sing= 'X' if current_sing == '0' else '0'
play_game(board)

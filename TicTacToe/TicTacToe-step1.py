# write your code here

# Messages
NEW_COORD = 'Enter the coordinates: '
ERR_OCCUPIED = 'This cell is occupied! Choose another one!'
ERR_NUMBERS = 'You should enter numbers!'
ERR_COORDINATES = 'Coordinates should be from 1 to 3!'

NOT_FINISHED = 'Game not finished'
DRAW = 'Draw'
WINS = 'wins'

BORDER = '|'
LINE = '---------'


# Functions
def print_game(game):
    print(LINE)
    for i in range(3):
        print(BORDER, ' '.join(game[i]), BORDER)
    print(LINE)

def validate_input(reponse, jeu):
    if not ''.join(reponse).isdigit():
        print(ERR_NUMBERS)
        return False
    elif int(reponse[0]) not in range(1, 4) or int(reponse[1]) not in range(1, 4):
        print(ERR_COORDINATES)
        return False
    elif jeu[int(reponse[0]) - 1][int(reponse[1]) - 1] in ['X', 'O']:
        print(ERR_OCCUPIED)
        return False
    return True

# Code
game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
start = [letter for letter in input('Enter the cells: ')]

nb_X = start.count('X')
nb_O = start.count('O')
if nb_X <= nb_O:
    jeu = 'X'
else:
    jeu = 'O'

k = 0

for i in range(3):
    for j in range(3):
        if start[k] != '_':
            game[i][j] = start[k]
        k += 1
print_game(game)

valide = False

while not valide:
    coord = input(NEW_COORD).split()
    valide = validate_input(coord, game)

game[int(coord[0]) - 1][int(coord[1]) - 1] = jeu

if (game[0][0] == game[0][1] == game[0][2] == jeu) or \
    (game[1][0] == game[1][1] == game[1][2] == jeu) or \
    (game[2][0] == game[2][1] == game[2][2] == jeu) or \
    (game[0][0] == game[1][0] == game[2][0] == jeu) or \
    (game[0][1] == game[1][1] == game[2][1] == jeu) or \
    (game[0][2] == game[1][2] == game[2][2] == jeu) or \
    (game[0][0] == game[1][1] == game[2][2] == jeu) or \
    (game[2][0] == game[1][1] == game[0][2] == jeu):
    print_game(game)
    print(jeu, WINS)
elif nb_X + nb_O + 1 < 9:
    print_game(game)
    print(NOT_FINISHED)
else:
    print_game(game)
    print(DRAW)


# Author: Ashley DeMott
# Project W2 Assignment: Tic-Tac-Toe

# constants of player name/tiles and grid layout
PLAYER_O = "o"
PLAYER_X = "x"
LINE_LENGTH = 3
LINE_SEPARATOR = "-+-+-\n"
ENTRY_SEPARATOR = "|"

# print grid, more flexible
grid_values = list(range(1,9+1))
for value in grid_values:
    # print value as first part of the line
    print(value, end='')
    0    
    # if it isn't the last value, need some formatting
    # TODO change value to value's index, for when xs and os are added to list (will become list of strings)
    if(value < grid_values[len(grid_values)-1]):
        if ((value) % LINE_LENGTH == 0):
            # print a horizontal separator
            print(f"\n{LINE_SEPARATOR}", end='')
        else:
            # print between values on same line
            print(ENTRY_SEPARATOR, end='')
    else:
        # end of the grid, no vertical separator
        print("\n")

# grid printed literally
print(f"1|2|3\n{LINE_SEPARATOR}4|5|6\n{LINE_SEPARATOR}7|8|9")

game_over = False   # continue the game until it is over
current_player = PLAYER_O   # choose the first player

while not game_over:
    # TODO: add input validation
    user_input = int(input(f"\n{current_player}'s turn to choose a square (1-9): "))
    
    # TODO: add player's move to board

    # TODO: figure out if there is a winner
    #       use line length to find if all in horizontal line are same x or o
    #       use line length to find if all in horizontal line are same x or o
    #       also make something with line length to find if diagonal are same x or o

    # current exit method, break will be used to keep current_player to declare winner
    if user_input == 0:
        break

    # no winner, change to the next player
    # uses ternary operator based on previous current_player (last_player)
    current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# keep current_player, will later change this to declare the winner
print(f"{current_player} ended the game")
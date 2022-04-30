# Author: Ashley DeMott
# Project: W2 Assignment: Tic-Tac-Toe
# Description: This program will allow the user to play a tic-tac-toe
#  game on whatever board size their heart desires. (I did put in a 
#  limit though, since it's just a really big board after a while)
#  If a player fills a row horizontally, vertically, or diagonally,
#  they win! Tile placements can't be repeated or placed on top of
#  by another player. At the end of the game, the winner will be
#  decided, or if the board is filled without a winner, the game
#  will be declared a draw. The winning combo will also be listed.

# TODO: Add color
COLORED = False
# Couldn't resolve issues with importing termcolor
# from termcolor import colored

# Constants for player names
PLAYER_O = "o"
PLAYER_X = "x"

# Constants for text colors - not implemented
PLAYER_O_COLOR = 'blue'
PLAYER_X_COLOR = 'red'
WINNER_COLOR = 'yellow'

# Grid size can change, but I put a range bc after
#  100 -scratch that 25 - it's a bit too much
GRID_RANGE = (1, 100)

def main():

    # Moved constants inside of main so grid size can be decided by the user.
    GRID_SIZE = get_valid_input("Please enter a grid size. Will create an X by X board", GRID_RANGE)

    # Create constants from the current grid size.
    GRID_NUM_TENS = find_tens_place(GRID_SIZE**2)
    LINE_SEPARATOR = create_horizontal_line(GRID_SIZE, GRID_NUM_TENS)
    ENTRY_SEPARATOR = "|"

    # Assign the grid values and print the grid.
    # (grid values are 1 more than the indexes)
    grid_values = list(range(1, (GRID_SIZE**2) + 1))
    print_grid(grid_values, GRID_NUM_TENS, LINE_SEPARATOR, ENTRY_SEPARATOR)

    # Continue the game until it is over.
    game_over = False
    # Player x will go first.
    current_player = PLAYER_X
    # Turn counter, if all moves are played without a win, game is a draw.
    num_turn = 0

    # While the game has not finished,
    while not game_over:
        # Count the number of turns
        num_turn += 1

        # Get a valid move from the player
        user_input = get_valid_move(current_player, grid_values)
        # print(f"Player {current_player} chose to place on {user_input}")

        # Adds the player's move to board
        grid_values[user_input - 1] = current_player

        # Prints the new board
        print_grid(grid_values, GRID_NUM_TENS, LINE_SEPARATOR, ENTRY_SEPARATOR)

        # Figure out if there is a winner, and show the winning numbers
        winning_combo = check_winner(current_player, grid_values)
        if len(winning_combo) == GRID_SIZE:
            print(f"{current_player} is the winner!")
            print("Winning combo: ", winning_combo)
            game_over = True # could just remove?
            break
        # Else if every move has been made, board is full.
        elif(num_turn == len(grid_values)):
            print("It's a draw!")
            game_over = True # could just remove? While True instead?
            break
        else:
            # There is no winner, change to the next player.
            # Uses ternary operator based on previous current_player (last_player)
            current_player = (PLAYER_O if current_player == PLAYER_X else PLAYER_X)

    # End message for the game
    print("Good game. Thanks for playing!")


def get_valid_input(message, num_range):
    """ Given a message (string) and a range of values (int)
         will repeatedly ask the user for an integer within
         the range until a vaild choice is made.
        Returns user's input (integer)
    """
    valid_input = False
    # While the input is not an int or within the range,
    while not valid_input:
        try:
            # Ask the user to choose an integer within the given range.
            user_input = int(input(f"{message} ({num_range[0]}-{num_range[1]}): "))
            # If value is in the range (inclusive),
            if user_input in range(num_range[0], num_range[1] + 1):
                 return user_input
            # Input was not within the range
            else:
                 print(f"Please enter a number between {num_range[0]} and {num_range[1]}.")
        except ValueError:
            # Error thrown by int(), user did not enter a integer
            print("Please enter a whole number.")
        except:
            print("An unexpected error has occured.")

def find_tens_place(find_tens):
    """ Returns the number of tens places (int)
         that a given value (int) has
    """
    # Finds the number of tens places in an integer
    # Used to adjust spacing for larger grids
    count = 0
    while find_tens > 9:        
        find_tens = find_tens//10
        count += 1
    return count

def create_horizontal_line(grid_length, grid_num_tens):
    """ Creates the string that will separate grid rows
         given the size/length of the grid (integer) and 
         the number of tens places the largest value in
         the grid has.
        Returns the horizontal line separator (string)
    """
    # Grid lines and spacing will adjust based on the grid size
    # Line size changes based on how many digits the largest number has
    # Initialize variables
    line_separator_string = ""
    dashes = "-"
    # Adds extra dashes for every tens place.
    for tens in range(grid_num_tens):
        dashes += "-"
    # Adds the '--+' string to represent rows
    #  and column intersections.
    for entries in range(grid_length - 1):
        line_separator_string += dashes + "+"
    # Adds dashes and a newline to end the grid
    line_separator_string += dashes + "\n"
    return line_separator_string

def get_valid_move(current_player, grid_values):
    """ Gets a valid user-inputed tictactoe move for
         the given grid. Disallows repeated moves.
        Returns user_input (integer)
    """
    # Initialize variables
    user_input = -1
    unique_choice = False
    message = f"\n{current_player}'s turn to choose a square"

    # Repeat until the user picks a value that hasn't been chosen yet
    while not unique_choice:
        # Get a valid square option (between 1 and the grid_size)
        user_input = get_valid_input(message, (1, len(grid_values)))
        # Check if the value has already been chosen
        try:
            # Value will be an int if it hasn't been chosen yet 
            # (otherwise will be char, 'x' or 'o')
            if isinstance(grid_values.index(user_input), int):
                unique_choice = True
        # Value is not in the grid, which means the value has already
        #  been chosen since the value is constrained between 1 and grid_size
        except ValueError:
            # Ask the user to enter a new choice
            print("Please choose a square that has not already been chosen.")
        except:
            print("An unexpected error has occured.")
    return user_input

def print_grid(grid_values, grid_num_tens, horizonal_separator, entry_separator):
    """ Prints the tic-tac-toe grid for the given grid values (list of ints/chars),
         number of tens places the largest number in the grid has (integer),
         a horizontal separator (string) to print between lines, and
         an entry separator to place between entries on the same row.
        Returns nothing (null)
    """
    # Grid length is square root of the length
    grid_length = len(grid_values)**(1/2)

    # TODO: Clear/refresh console

    # if between 0 and 9 (not including 9)
    for index in range(0, len(grid_values)):
        # Print the value as first part of the line
        # ERROR: Colors values based on player
        if(COLORED and grid_values[index] == PLAYER_O):
            print(colored(PLAYER_O, PLAYER_O_COLOR), end='')
        elif(COLORED and grid_values[index] == PLAYER_X):
            print(colored(PLAYER_X, PLAYER_X_COLOR), end='')
        else:
            print(grid_values[index], end='')
        # If it isn't the last value, some formatting is needed        
        if(index < (len(grid_values) - 1)):
            # If it is the end of the grid line,
            # (The +1 starts the numbers at 1 (1 to gridsize))
            if ((index + 1) % grid_length == 0):
                # Print a horizontal separator
                print(f"\n{horizonal_separator}", end='')
            else:
                # Print vertical separator between values on the same line.
                extra_spaces = ""
                # If the value is still an integer,
                if(isinstance(grid_values[index], int)):
                    # Add spaces based on how many tens places the number has.
                    for num in range(grid_num_tens - (find_tens_place(grid_values[index]))):
                        extra_spaces += " "
                else:
                    # Otherwise, add spaces for as many tens places the largest number has.
                    for num in range(grid_num_tens):
                        extra_spaces += " "
                # Print the extra_spaces and the separator.
                print(f"{extra_spaces}{entry_separator}", end='')
        else:
            # End of the grid, finish the line.
            print("\n")

def check_winner(current_player, grid_values):
    """ Checks if there is a winner for the tic-tac-toe
         game given the last player to place a piece (char),
         and the values on the grid (list of ints/chars)
        Returns winning_combo (list of ints) that led to the win
    """
    
    # Initialize a counter for player peices in a row.
    count = 0
    winning_combo = []
    # Will always be a whole number, cast float to int
    grid_length = int(len(grid_values)**(1/2))

    # Check each row.
    for row in range(grid_length):
        count = 0
        winning_combo = []
        # Check going left to right.
        for column in range(grid_length):
            index = column + (row * grid_length)
            # Count the player peices, list for a win.
            if(grid_values[index] == current_player):
                count += 1
                winning_combo.append(index + 1)
        # If a full row is all the same player, winner!
        if(count == grid_length):
            return winning_combo
    
    # Checks each Column.
    for column in range(grid_length):
        count = 0
        winning_combo = []        
        # Check going top to bottom.
        for row in range(grid_length):
            index = (row * grid_length) + column
            # Count player peices, list for a win.
            if(grid_values[index] == current_player):
                count += 1
                winning_combo.append(index + 1)
        # If a full column is all the same player, winner!
        if(count == grid_length):
            return winning_combo
    # Reset count and winning combo. 
    count = 0
    winning_combo = []

    # Checks first diagonal (left to right)
    for row in range(grid_length):
        # Checks each row, starts from left
        # Add to list incase of a win
        index = (row * grid_length) + (row)
        if(grid_values[index] == current_player):
            count += 1
            winning_combo.append(index + 1)
    if(count == grid_length):
        return winning_combo
    # Reset count and winning combo.
    count = 0
    winning_combo = []

    # Checks second diagonal (right to left)
    for row in range(grid_length):
        # Checks each row, starts from right (end)
        # Add to list incase of a win
        index = (row * grid_length) + ((grid_length - 1) - row)
        if(grid_values[index] == current_player):
            count += 1
            winning_combo.append(index + 1)
    if(count == grid_length):
        return winning_combo

    # If none of the win conditions have been met, no winner. Winning_combo will not be complete
    return winning_combo

# When the program is run directly, it will run the main funciton.
if __name__ == "__main__":
    main()
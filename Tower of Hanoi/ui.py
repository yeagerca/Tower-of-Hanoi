# This is a sample Python script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.


# global variables
# store game state
num_towers = 3
towers = [[3, 2, 1], [4], [5]]
max_height = len(towers[0]) + len(towers[1]) + len(towers[2])  # assuming it uses every integer from 1 to n


def total_width():
    """
    :return: Character length of the highest number, multiplied by the number of towers.
    """
    return tower_width() * num_towers


def tower_width():
    return len(str(max_height))


def right_pad_vertical_towers(lines, width):

    return


def print_welcome():
    print('Welcome to Tower of Hanoi.\n')


def print_intro():
    print('In this game there are three towers that are constructed with blocks of unique size.\n'
          'The "blocks" are represented by numbers that indicate the block\'s size. '
          'The "towers" are represented as a list of blocks.\n'
          'Blocks may only be placed on top of blocks that are larger than itself. '
          'An empty tower can accept any block.\n'
          'The game begins with one fully constructed tower at the left-most position.\n'
          'The goal of the game is to move that entire tower, one block at a time, to the right-most position.\n')


def transpose_tower_vertical():
    """
    TODO: Refactor name or make it do the correct job. Currently it just inverts the list and fills empty spaces.
    Example Horizontal (storage):   \n
    A 4 3                           \n
    B 1                             \n
    C 2                             \n
    Example Vertical (display):     \n
    3                               \n
    4                               \n
    A B C                           \n
    :return: list<list> = [[], [], []]
    """
    vert = [[], [], []]
    for h in range(max_height):
        t_index = 0
        for t in towers:
            if len(t) > h:
                vert[t_index].insert(0, t[h])
            else:
                vert[t_index].insert(0, " ")
            t_index += 1
    print(towers)
    print(vert)
    return vert


def print_game_state_vertical():
    vert = transpose_tower_vertical()

    # get numbers in each line as strings
    lines = ["", "", ""]
    for h in range(max_height):
        index = 0
        for v in vert:
            lines[index] = str(v[h])
            index += 1
        print(lines)

    # total_width()  # find the maximum character length of the bottom row based on what the highest number is.
    # tower_width()  # determine standardized width for each tower in characters.
    # TODO create functionalities for the comments below.
    right_pad_vertical_towers(lines, tower_width())  # right-pad each line segment using blank spaces (individual block numbers) to left-align everything.
    # insert an additional blank space to separate towers.
    # right-pad tower labels
    # print everything

    return


if __name__ == '__main__':
    print_welcome()
    print_intro()

    # TODO print game state nicely
    print_game_state_vertical()

    # TODO prompt for user input about which tower to move from
    # TODO accept user input about which tower to move from
    # TODO prompt user input about which tower to move to
    # TODO accept user input about which tower to move to
    # TODO validate user decision within game rules. Print success/fail message and restart prompts.

    # TODO remove print debugs when finished


import random

END = "\033[0m"
Red = "\033[0;31m"
Green = "\033[0;32m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"


def player_x(player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select):
    print(tic_tac_toe_chart)
    if player == "X":
        position = input(Blue + "Select a position you would like to place X:" + END)
        delete = list_of_positions_for_bot_to_select.index(position)
        list_of_positions_for_bot_to_select.pop(delete)
        replace = tic_tac_toe_chart.find(position)
        tic_tac_toe_chart = (
            tic_tac_toe_chart[:replace] + "X" + tic_tac_toe_chart[replace + 1 :]
        )
        return did_x_win(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )
    elif Bot == "X":
        print(Red + "Its bots turn" + END)
        chosen_position = random.choice(list_of_positions_for_bot_to_select)
        spot_position_is_in = list_of_positions_for_bot_to_select.index(chosen_position)
        list_of_positions_for_bot_to_select.pop(spot_position_is_in)
        replace = tic_tac_toe_chart.find(chosen_position)
        tic_tac_toe_chart = (
            tic_tac_toe_chart[:replace] + "X" + tic_tac_toe_chart[replace + 1 :]
        )
        return did_x_win(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )


def player_o(player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select):
    print(tic_tac_toe_chart)
    if player == "O":
        position = input(Blue + "Select a position you would like to place O:" + END)
        delete = list_of_positions_for_bot_to_select.index(position)
        list_of_positions_for_bot_to_select.pop(delete)
        replace = tic_tac_toe_chart.find(position)
        tic_tac_toe_chart = (
            tic_tac_toe_chart[:replace] + "O" + tic_tac_toe_chart[replace + 1 :]
        )
        return did_o_win(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )
    elif Bot == "O":
        print(Red + "Its bots turn" + END)
        chosen_position = random.choice(list_of_positions_for_bot_to_select)
        spot_position_is_in = list_of_positions_for_bot_to_select.index(chosen_position)
        list_of_positions_for_bot_to_select.pop(spot_position_is_in)
        replace = tic_tac_toe_chart.find(chosen_position)
        tic_tac_toe_chart = (
            tic_tac_toe_chart[:replace] + "O" + tic_tac_toe_chart[replace + 1 :]
        )
        return did_o_win(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )


# checks to see if player X won if not then keeps game keeps playing
def did_x_win(player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select):
    position_one = tic_tac_toe_chart[0]
    position_two = tic_tac_toe_chart[2]
    position_three = tic_tac_toe_chart[4]
    position_four = tic_tac_toe_chart[7]
    position_five = tic_tac_toe_chart[9]
    position_six = tic_tac_toe_chart[11]
    position_seven = tic_tac_toe_chart[13]
    position_eight = tic_tac_toe_chart[15]
    position_nine = tic_tac_toe_chart[17]
    if player == "X":
        # 1 2 3 is filled with X
        if position_one == "X" and position_two == "X" and position_three == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 4 5 6 filled with X
        elif position_four == "X" and position_five == "X" and position_six == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 7 8 9 filled with X
        elif position_seven == "X" and position_eight == "X" and position_nine == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "X" and position_four == "X" and position_seven == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_two == "X" and position_five == "X" and position_eight == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "X" and position_six == "X" and position_nine == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "X" and position_five == "X" and position_nine == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "X" and position_five == "X" and position_seven == "X":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif (
            position_one != "1"
            and position_two != "2"
            and position_three != "3"
            and position_five != "4"
            and position_six != "6"
            and position_seven != "7"
            and position_eight != "8"
            and position_nine != "9"
        ):
            print(tic_tac_toe_chart)
            print(Green + "its a tie" + END)
            return play_again()
        else:
            return player_o(
                player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
            )

    elif Bot == "X":
        # 1 2 3 is filled with X
        if position_one == "X" and position_two == "X" and position_three == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 4 5 6 filled with X
        elif position_four == "X" and position_five == "X" and position_six == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 7 8 9 filled with X
        elif position_seven == "X" and position_eight == "X" and position_nine == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "X" and position_four == "X" and position_seven == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_two == "X" and position_five == "X" and position_eight == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "X" and position_six == "X" and position_nine == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "X" and position_five == "X" and position_nine == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "X" and position_five == "X" and position_seven == "X":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif (
            position_one != "1"
            and position_two != "2"
            and position_three != "3"
            and position_five != "4"
            and position_six != "6"
            and position_seven != "7"
            and position_eight != "8"
            and position_nine != "9"
        ):
            print(tic_tac_toe_chart)
            print(Green + "its a tie" + END)
            return play_again()
        else:
            return player_o(
                player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
            )


# checks to see if player O won if not then keeps game keeps playing
def did_o_win(player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select):
    position_one = tic_tac_toe_chart[0]
    position_two = tic_tac_toe_chart[2]
    position_three = tic_tac_toe_chart[4]
    position_four = tic_tac_toe_chart[7]
    position_five = tic_tac_toe_chart[9]
    position_six = tic_tac_toe_chart[11]
    position_seven = tic_tac_toe_chart[13]
    position_eight = tic_tac_toe_chart[15]
    position_nine = tic_tac_toe_chart[17]
    if player == "O":
        # 1 2 3 is filled with X
        if position_one == "O" and position_two == "O" and position_three == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 4 5 6 filled with X
        elif position_four == "O" and position_five == "O" and position_six == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 7 8 9 filled with X
        elif position_seven == "O" and position_eight == "O" and position_nine == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "O" and position_four == "O" and position_seven == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_two == "O" and position_five == "O" and position_eight == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
        elif position_three == "O" and position_six == "O" and position_nine == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "O" and position_five == "O" and position_nine == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "O" and position_five == "O" and position_seven == "O":
            print(Blue + "You Win!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif (
            position_one != "1"
            and position_two != "2"
            and position_three != "3"
            and position_five != "4"
            and position_six != "6"
            and position_seven != "7"
            and position_eight != "8"
            and position_nine != "9"
        ):
            print(Green + "its a tie" + END)
            print(tic_tac_toe_chart)
            return play_again()
        else:
            return player_x(
                player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
            )
    elif Bot == "O":
        # 1 2 3 is filled with X
        if position_one == "O" and position_two == "O" and position_three == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 4 5 6 filled with X
        elif position_four == "O" and position_five == "O" and position_six == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        # 7 8 9 filled with X
        elif position_seven == "O" and position_eight == "O" and position_nine == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "O" and position_four == "O" and position_seven == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_two == "O" and position_five == "O" and position_eight == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
        elif position_three == "O" and position_six == "O" and position_nine == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_one == "O" and position_five == "O" and position_nine == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif position_three == "O" and position_five == "O" and position_seven == "O":
            print(Red + "The Bot Wins!" + END)
            print(tic_tac_toe_chart)
            return play_again()
        elif (
            position_one != "1"
            and position_two != "2"
            and position_three != "3"
            and position_five != "4"
            and position_six != "6"
            and position_seven != "7"
            and position_eight != "8"
            and position_nine != "9"
        ):
            print(Green + "its a tie" + END)
            print(tic_tac_toe_chart)
            return play_again()
        else:
            return player_x(
                player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
            )


def x_or_o(player):
    tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
    list_of_positions_for_bot_to_select = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if player == "x" or player == "X":
        player = "X"
        Bot = "O"
        print("You chose X")
        return player_x(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )
    elif player == "o" or player == "O":
        player = "O"
        Bot = "X"
        print("You chose O")
        return player_x(
            player, Bot, tic_tac_toe_chart, list_of_positions_for_bot_to_select
        )
    else:
        player = str(input(Red + "You must choose X or O:" + END))
        return x_or_o(player)


def play_again():
    print(Purple + "This is a new game" + END)
    player = str(input("Would you like to be X or O:"))
    x_or_o(player)


player = str(input("Would you like to be X or O:"))
x_or_o(player)

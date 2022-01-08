END = '\033[0m'
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple

def player_x(player, Bot, tic_tac_toe_chart,list_of_positions_for_bot_to_select):
    print(tic_tac_toe_chart) 
    if player == "X":
        position = input ("select a position you would like to place X:")
        delete = list_of_positions_for_bot_to_select.index(position)
        list_of_positions_for_bot_to_select.pop(delete)
        print (list_of_positions_for_bot_to_select) ### to delete
        replace = tic_tac_toe_chart.find(position)
        tic_tac_toe_chart = tic_tac_toe_chart[:replace] + 'X' + tic_tac_toe_chart[replace+1:]
        print(tic_tac_toe_chart) #### delete?
    elif Bot == "X":
        print ("will do next")


def x_or_o (player):
    tic_tac_toe_chart = "1 2 3 \n4 5 6\n7 8 9\n"
    list_of_positions_for_bot_to_select = ["1","2","3","4","5","6","7","8","9"]
    if player == "x" or player == "X":
        player = "X"
        Bot = "O"
        print("You chose X")
        return player_x(player, Bot, tic_tac_toe_chart,list_of_positions_for_bot_to_select)
    elif player == "o" or player == "O":
        player = "O"
        Bot = "X"
        print("You chose O")
        return player_x(player, Bot, tic_tac_toe_chart,list_of_positions_for_bot_to_select)
    else:
        player = str(input(Red +"You must choose X or O:"+ END)) 
        return x_or_o (player)

player = str(input("Would you like to be X or O:")) 
x_or_o (player)

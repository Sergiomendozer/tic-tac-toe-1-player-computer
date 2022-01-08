#jhfshgis
END = '\033[0m'
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple

def x_or_o (player):
    if player == "x" or player == "X":
        print("You chose X")
    elif player == "o" or player == "O":
        print("You chose O")
    else:
        player = str(input(Red +"You must choose X or O:"+ END)) 
        return x_or_o (player)



player = str(input("Would you like to be X or O:")) 
x_or_o (player)


# Online Python - IDE, Editor, Compiler, Interpreter

theBoard = {'1': ' ', '2': ' ', '3': '2', '4': ' ',
            '5': ' ', '6': '1', '7': ' ', '8': ' ',
            '9': ' ', '10': '4', '11': ' ', '12': ' ',
            '13': ' ', '14': ' ', '15': ' ', '16': '3'}
board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board) -> object:
    print(board['1'] + '|' + board['2'] + '||' + board['3'] + '|' + board['4'])
    print('-+-||-+-')
    print(board['5'] + '|' + board['6'] + '||' + board['7'] + '|' + board['8'])
    print('=+=||=+=')
    print(board['9'] + '|' + board['10'] + '||' + board['11'] + '|' + board['12'])
    print('-+-||-+-')
    print(board['13'] + '|' + board['14'] + '||' + board['15'] + '|' + board['16'])


print("Positions on board")
print("1 |2 ||3 |4 ")
print("5 |6 ||7 |8 ")
print("9 |10||11|12")
print("13|14||15|16")
print("\t\t\tGame Begins\n\n\n")


def game():
    printBoard(theBoard)
    for i in range(12):

        print("Type the digit between 1 to 4 and position to digit")

        dig = input("digit-")
        pos = input("Position(1-16):-")

        if theBoard[pos] == ' ':
            theBoard[pos] = dig

        else:
            print("That position is already filled!\n Put the digit in another position")
            continue
        printBoard(theBoard)
        if theBoard['1'] != " " and theBoard['2'] != " " and theBoard['3'] != " " and theBoard['4'] != " " \
                and theBoard['5'] != " " and theBoard['6'] != " " and theBoard['7'] != " " and theBoard['8'] != " " \
                and theBoard['9'] != " " and theBoard['10'] != " " and theBoard['11'] != " " and theBoard['12'] != " " \
                and theBoard['13'] != " " and theBoard['14'] != " " and theBoard['15'] != " " and theBoard['16'] != " ":
            print("The Game is Over.")
            print("The correct solution is :-")
            print("4|3||2|1")
            print("-+-||-+-")
            print("2|1||3|4")
            print("=+=||=+=")
            print("3|4||1|2")
            print("-+-||-+-")
            print("1|2||4|3")

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for keys in board_keys:
            theBoard[keys] = " "
            theBoard['3'] = "2"
            theBoard['6'] = "1"
            theBoard['10'] = "4"
            theBoard['16'] = "3"

        game()

game()
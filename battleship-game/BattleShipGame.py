from random import randint

print("BATTLESHIP GAME\nThe objective is to sink the opponent's ships before the opponent sinks yours.\nNOTE, If you 'quite' the opponent wins the game.")

#creating an empty list for game chart and a dictionary to assign number of hits
game_chart = []
player1 = { "name": "Player 1", "wins": 0, "lose": 0 }
player2 = { "name": "Player 2", "wins": 0, "lose": 0 }
computer= { "name": "computer", "wins": 0, "lose": 0 }
total_turns = 0

#first am drawing the game chart of 5 x 5 for both players and computer
def buildGameChart(chart):
    for item in range(5):
        chart.append([" "] * 5)

def showChart(chart):
    for row in chart:
        print(" ".join(row))

#define ship location to fire missil
def stream_game(chart):
    del chart[:]
    buildGameChart(chart)
    showChart(chart)
    #players enter ship positions here
    #ship_col = int(input(""))
    #ship_col = str(input(""))
    ship_col = randint(1, len(chart))
    ship_row = randint(1, len(chart[0]))
    return {
        'ship_col': ship_col,
        'ship_row': ship_row,
    }
ship_points = stream_game(game_chart)

#how players alternate
def players_turns():
    if total_turns % 2 == 0:
        return player2
    else:
        return player1

def player_comp_turn():
    if total_turns % 2 == 0:
        return computer
    else:
        return player1

#repeat game after its over
def play_game_again():
    feedback = input("Would you like to play again?").lower()
    if feedback == "yes" or feedback == "y":
        total_turns = 0
        ship_points = stream_game(game_chart)
    else:
        print("Thank you for playing!!!")
        exit()

#number of games to play
def no_of_games():
    for games in range(5):
        games += 1
        for turns in range(5):
            total_turns += 1
            if players_turns() == player1:
                print("Player One")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player1, game_chart
                )
            elif players_turns() == player2:
                print("Player Two")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player2, game_chart
                )
            else:
                continue
            if total_turns == 5 and players_turns() == player1:
                print("The game is a draw")
                play_game_again()
            elif total_turns == 5 and players_turns() == player2:
                print("The game is a draw")
                play_game_again()
            else:
                continue

# 1st condition when the game launches
game_choice = int(input("Input 1 for 1-player game or 2 for 2-player game: "))
if game_choice == 1:
    print("Player 1 vs Computer")
elif game_choice == 2:
    #player 1 vs player 2
    #player 1 inputs 5 ship positions
    print("Player 1 Enter Your 5 Positions")
    for p1_ship in range(5):   
        p1_ship = input("Player 1 enter position for your ship: ")
    
    #this loop will make player 2 not to see player 1's move
    for symbol in "********************************************************************************************************":
        print(symbol*2)
    
    #player 2 inputs 5 ship positions
    print("Player 2 Enter Your 5 Positions")
    for p2_ship in range(5):
        p2_ship = input("Player 2 enter position for your ship: ")
        
    def input_check(ship_row, ship_col, player, chart):
        guess_col = 0
        guess_row = 0
        while True:
            try:
                guess_row = int(input("Row:")) - 1
                guess_col = int(input("Col:")) - 1
            except ValueError:
                print("Invalid position, or missile already thrown there. Try again: ")
                continue
            else:
                break
        match = guess_row == ship_row - 1 and guess_col == ship_col - 1
        not_on_game_chart = (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)

        if match:
            player["Target hit!"] += 1
            print("Congratulations! You sunk my battleship!\nGAME OVER")
            play_game_again()
        elif not match:
            if not_on_game_chart:
                print("Invalid position, or missile already thrown there. Try again:")
            elif chart[guess_row][guess_col] == "X":
                print("Invalid position, or missile already thrown there. Try again: ")
            else:
                print("Target missed!")
                chart[guess_row][guess_col] = "X"
            showChart(game_chart)
        else:
            return 0


    #this loop will make player who starts the match not to see player 2's ship position
    for symbol in "**********************************************************************************************************":
        print(symbol*2)
    print("START GAME")
    print("FOR NOW ENTER NUMBERS ONLY FOR ROWS AND COLUMN")
    #total number of games to play
    for games in range(3):
        games += 1
        for turns in range(6):
            total_turns += 1
            if players_turns() == player1:
                print("Player One")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player1, game_chart
                )
            elif players_turns() == player2:
                print("Player Two")
                input_check(
                    ship_points['ship_row'],
                    ship_points['ship_col'],
                    player2, game_chart
                )
            else:
                continue
            if total_turns == 5 and players_turns() == player1:
                print("The game is a draw")
                play_game_again()
            elif total_turns == 5 and players_turns() == player2:
                print("The game is a draw")
                play_game_again()
            else:
                continue
else:
    print("Sorry!!! Enter a valid choice. Try again? ")
    game_choice = int(input("Input 1 for 1-player game or 2 for 2-player game: "))

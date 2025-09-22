# @author Qusai Elwazir
import curses
import board_processor
import move_analyzer
import random
import string
import tkinter as tk
import board_processor



# scr = curses.initscr()
# scr.keypad(0)
# curses.noecho()

# scr.addstr("hello world")
# scr.refresh()
# scr.getch()

# curses.endwin()
this_state = board_processor.get_board_from_list(
                                        [["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""]])
def reset_board():
    global this_state
    this_state = board_processor.get_board_from_list(
                                        [["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                        ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""]])
    



def get_random_letters(n: int) -> str:
    letters = ""
    for i in range(n):
        letters += random.choice(string.ascii_lowercase)
    return letters 

def bot_move(game_state: board_processor.Game_State) -> tuple:
    hand = get_random_letters(7)
    bot_move = move_analyzer.find_maximal_move(hand, game_state)
    return (bot_move, hand) 

def update_board(move, game_state):
    for idx in range(len(move.word)):
        game_state.board[move.span[idx][0]][move.span[idx][1]].occupant = move.word[idx]
        game_state.board[move.span[idx][0]][move.span[idx][1]].is_empty = False

def print_board():
    print()
    print("   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14")
    for i in range(len(this_state.board)):
        if i < 10:
            print(str(i) + " ", end="")
        else:
            print(i, end="")
        for j in range(len(this_state.board)):
            if(this_state.board[i][j].occupant == ""):
                if this_state.board[i][j].word_multiplier == 2:
                    print("[dw]", end="")
                elif this_state.board[i][j].word_multiplier == 3:
                    print("[tw]", end="")
                elif this_state.board[i][j].letter_multiplier == 2:
                    print("[dl]", end="")
                elif this_state.board[i][j].letter_multiplier == 3:
                    print("[tl]", end="")
                else:
                    print("[  ]", end="")
            else:
                print("[ " + this_state.board[i][j].occupant.upper() + "]", end="")
        print(" ")

def play_game(n: int) -> int:
    p1_score = 0
    p2_score = 0
    #play n turns demo
    for i in range(n): #TODO make first move possilbe!
        
        move = bot_move(this_state)
        print("possible_words with hand: [" + move[1] + "]:")
        all_moves = move_analyzer.find_all_moves(move[1], this_state)
        for j in range(len(all_moves)):
            print("(\""+ all_moves[j].word + "\" idx:[" + str(all_moves[j].span[0][0]) + "][" + str(all_moves[j].span[0][1]) + "] score:" +  str(all_moves[j].score) + "), ", end="")
            if j != 0 and j % 3 == 0:
                print()
        print()

        update_board(move[0], this_state)
        print_board()
        print("turn: " + str(i + 1))
        if i % 2 == 1:
            print("P1 played: " + move[0].word)
            p1_score += move[0].score
        else:
            print("P2 played: " + move[0].word)
            p2_score += move[0].score
        print("scoring: " + str(move[0].score))
        print("P1: " + str(p1_score) + " P2: " + str(p2_score))
        print()

    return (p1_score + p1_score) / 2

def average_score(moves: int, games: int):
    scores = 0  
    for i in range(games):
        reset_board()
        scores += play_game(moves)

    print("average score: " + str(scores / games))# print all moves for n turns
    print()

average_score(5, 50) #aveage score per move in the first 4 moves of a game
# play_game(20) #50 turn game


# #!!GUI




# # HandLabel.pack()

# # Add a button widget


# hand = get_random_letters(7).upper()
# potential_hand = hand
# curr_held = ""
# potential_word = ""
# potential_move_span = list()
# potential_move: move_analyzer.Move # use find_neighbor_orientation(i:int, j:int, game_state: board_processor.Game_State) -> int: to find orientation
# hand_buttons = list()
# board_buttons = list()

# def hand_button(i: int):
#     global hand
#     global curr_held
#     curr_held = hand_buttons[i].cget("text")
#     hand_buttons[i].config(text=" ")
#     print(curr_held)

# def board_button(i: int, j: int):
#     global curr_held
#     global potential_move_span
#     global potential_word
#     global potential_hand
#     global board_buttons
#     global SubmitButton
#     # potential_hand.replace(curr_held, " ")

#     potential_word += curr_held
#     potential_move_span.append((i,j))
#     board_buttons[i][j].config(text=f"{curr_held}")
#     curr_held = ""


# def SubmitButton():
#     global potential_move_span
#     global potential_word
#     global potential_hand

#     move = move_analyzer.Move(potential_move_span, potential_word)

#     if move_analyzer.is_legal_move(move):
#         update_board(move)
#         update_hand()

# def update_board(move):
#     for idx in range(len(move.word)):
#         this_state.board[move.span[idx][0]][move.span[idx][1]].occupant = move.word[idx]
#         this_state.board[move.span[idx][0]][move.span[idx][1]].is_empty = False
#     for i in range(15):
#         for j in range(15):
#             curr_button = board_buttons[i][j]
#             letter = ""
#             if(this_state.board[i][j].occupant == ""):
#                     if this_state.board[i][j].word_multiplier == 2:
#                         letter = "DW"
#                     elif this_state.board[i][j].word_multiplier == 3:
#                         letter = "TW"
#                     elif this_state.board[i][j].letter_multiplier == 2:
#                         letter = "DL"
#                     elif this_state.board[i][j].letter_multiplier == 3:
#                         letter = "TL"
#                     else:
#                         letter = ""
#             else:
#                     letter = this_state.board[i][j].occupant.upper()
#             curr_button.config(text=f"{letter}")

# def update_hand():
#     global potential_hand
#     for i in range(7):
#         hand_buttons[i].config(text=f"{potential_hand[i]}")
#     print(potential_hand)

# def init():
#     global hand_buttons
#     global board_buttons 
#     global this_state
#     global SubmitButton

#     hand_buttons = [None for i in range(7)]

#     for i in range(7):
#         current_button = tk.Button(HandFrame,
#                                 text = f"{hand[i]}",
#                                 font=("Interstate Bold", 10),
#                                 height = 0,
#                                 width = 3,
#                                 padx=7,
#                                 pady=3,
#                                 command=lambda i=i,:hand_button(i))

#             #Grid occurs on a new line
#         current_button.grid(row=0, column=i, padx=0, pady=0)
#         hand_buttons[i]= current_button
    
#     SubmitButton = tk.Button(HandFrame, text="Submit Move", command=SubmitButton())
#     SubmitButton.grid(row=0, column=8, padx=0, pady=0)

#     board_buttons = [[None for i in range(15)] for j in range(15)]

#     for i in range(15):
#         for j in range(15):
#             letter = ""
#             if(this_state.board[i][j].occupant == ""):
#                     if this_state.board[i][j].word_multiplier == 2:
#                         letter = "DW"
#                     elif this_state.board[i][j].word_multiplier == 3:
#                         letter = "TW"
#                     elif this_state.board[i][j].letter_multiplier == 2:
#                         letter = "DL"
#                     elif this_state.board[i][j].letter_multiplier == 3:
#                         letter = "TL"
#                     else:
#                         letter = ""
#             else:
#                     letter = this_state.board[i][j].occupant.upper()

#             current_button = tk.Button(BoardFrame,
#                                 text = f"{letter}",
#                                 font=("Interstate Bold", 8),
#                                 height = 0,
#                                 width = 3,
#                                 padx=7,
#                                 pady=3,
#                                 command=lambda i=i, j=j:board_button(i,j))

#             #Grid occurs on a new line
#             current_button.grid(row = i, column = j, padx=0, pady=0)
#             board_buttons[i][j] = current_button

# root = tk.Tk()
# BoardFrame = tk.Frame(root, padx= 55)
# BoardFrame.grid()

# HandFrame = tk.Frame(root, padx= 55, pady=15)
# HandLabel = tk.Label(HandFrame, text="hand:")
# HandFrame.grid()
# root.geometry("600x600+500+0")
# init()

# root.mainloop()
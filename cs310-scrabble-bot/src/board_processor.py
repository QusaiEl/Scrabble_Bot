# @author Qusai Elwazir

import dictionary_processor

class Space:
    occupant: str
    letter_multiplier: int
    word_multiplier: int
    is_empty: bool
    word_multiplier: int
    
    def __init__(self, occupant: str, letter_multiplier: int, word_multiplier: int, is_empty: bool):
        self.occupant = occupant
        self.letter_multiplier = letter_multiplier
        self.word_multiplier = word_multiplier
        self.is_empty = is_empty


class Game_State:
    board = list()
    move_history = list()
    language: tuple

    def __init__(self, board, language):
        self.board = board
        self.language = language

def get_board_from_list(board: list) -> Game_State: #TODO
    i = 0
    j = 0
    new_game_state = Game_State(board, dictionary_processor.create_language("alphabet.txt", "dictionary.txt")) #!!HARDCODED FOR NOW
    standard_board = [["31M","111", "111", "12M", "111", "111", "111", "31M", "111", "111", "111", "12M", "111", "111", "31M"],
                      ["111","21M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111", "111", "111", "21M", "111"],
                      ["111","111", "21M", "111", "111", "111", "12M", "111", "12M", "111", "111", "111", "21M", "111", "111"],
                      ["12M","111", "111", "21M", "111", "111", "111", "12M", "111", "111", "111", "21M", "111", "111", "12M"],
                      ["111","111", "111", "111", "21M", "111", "111", "111", "111", "111", "21M", "111", "111", "111", "111"],
                      ["111","13M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111"],
                      ["111","111", "12M", "111", "111", "111", "12M", "111", "12M", "111", "111", "111", "12M", "111", "111"],
                      ["31M","111", "111", "12M", "111", "111", "111", "21M", "111", "111", "111", "12M", "111", "111", "31M"],
                      ["111","111", "12M", "111", "111", "111", "12M", "111", "12M", "111", "111", "111", "12M", "111", "111"],
                      ["111","13M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111"],
                      ["111","111", "111", "111", "21M", "111", "111", "111", "111", "111", "21M", "111", "111", "111", "111"],
                      ["12M","111", "111", "21M", "111", "111", "111", "12M", "111", "111", "111", "21M", "111", "111", "12M"],
                      ["111","111", "21M", "111", "111", "111", "12M", "111", "12M", "111", "111", "111", "21M", "111", "111"],
                      ["111","21M", "111", "111", "111", "13M", "111", "111", "111", "13M", "111", "111", "111", "21M", "111"],
                      ["31M","111", "111", "12M", "111", "111", "111", "31M", "111", "111", "111", "12M", "111", "111", "31M"]]
    for i in range(len(standard_board)):
        for j in range(len(standard_board)):
            new_game_state.board[i][j] = Space(occupant=board[i][j].lower(), letter_multiplier=int(standard_board[i][j][1]), 
                                               word_multiplier=int(standard_board[i][j][0]), is_empty=board[i][j] == "")
        
    return new_game_state

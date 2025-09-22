# @author Qusai Elwazir

import dictionary_processor
import dictionary_searcher
import board_processor

class Move:
    orientation: bool = False
    i = 0
    j = 0
    word = ""
    score = 0
    intersection = 0
    span = None
    start_idx = 0

    # dir == true means veritcal dir == false means horizontal
    def __init__(self, orientation: bool = False, i:int = 0, j:int = 0, word:str= "", game_state: board_processor.Game_State = None, fm: bool = False):
        # bot move creation
        if(word.find(game_state.board[i][j].occupant) == -1):
            return None
        self.orientation = orientation # may take the value "vertical", "horizotal", or "other"
        self.i = i
        self.j = j
        self.word = word.lower()

        if fm == True:
            self.intersection = int(len(self.word) / 2)
        else:
            self.intersection = self.word.index(game_state.board[self.i][self.j].occupant)  

        self.start_idx = move_start(self.i, self.j, orientation, self.intersection)
        self.span = find_span(self.i, self.j, self.start_idx, self.orientation, self.word)

def move_start(i, j, orientation, intersection):
    start_idx = 0
    if orientation == True: #vertical
        if i - intersection >= 0:
            start_idx = i - intersection
    elif orientation == False: #horizontal 
        if j - intersection >= 0:
            start_idx = j - intersection
    return start_idx

def find_span(i, j, start_idx, orientation, word):
    idx = start_idx
    span = list()
  
    if orientation == True: #vertical
        for letter in word:
            span.append((idx, j))
            idx += 1
    elif orientation == False: #horizontal 
        for letter in word:
            span.append((i, idx))
            idx += 1
    return span

# play object contains if a given play is horizonal or vertical, the index at which the play intersects with the island, and the word itself
def find_maximal_move(hand:list, game_state: board_processor.Game_State) -> Move: #TODO CHANGE GAMESTATE TO JUST BOARD
    all_moves = find_all_moves(hand, game_state)
    curr_max = 0
    max_move: Move = Move(False, 7, 7, "", game_state) #defualt move in case of no legal play
    max_move.score = 0
    if board_is_empty(game_state.board):
        for move in all_moves:
            if(len(move.word) > curr_max):
                max_move = move
                curr_max = len(move.word)
        return max_move

    for move in all_moves:
        if(move.score > curr_max):
            max_move = move
            curr_max = move.score
    return max_move

def find_all_moves(hand: list, game_state: board_processor.Game_State):
    all_moves = list()
    row: int = 0
    col: int = 0
    neighbors = list()

    if board_is_empty(game_state.board): # first move condition
        return find_first_moves(hand, game_state)

    for row in range(len(game_state.board)):
        for col in range(len(game_state.board)):
            if(game_state.board[row][col].is_empty): #!! adjacency move
                words = dictionary_searcher.get_all_words(hand, game_state.language)
                all_moves += find_adjacency_moves(words, row, col, hand, game_state)
                continue
            neighbors = find_neighbors(row, col, game_state)
            if((neighbors[1] and not neighbors[0]) or (neighbors[3] and not neighbors[2])): #corner and ends
                all_moves += find_addition_moves(row, col, hand, game_state)
            elif(neighbors[1] or neighbors[0]) ^ (neighbors[3] or neighbors[2]): # middles
                all_moves += find_intersection_moves(row, col, hand, game_state)
    return all_moves

def find_first_moves(hand, game_state):
    first_moves = list()
    words = dictionary_searcher.get_all_words(hand, game_state.language)
    for word in words:
        curr_move = Move(False, 7, 7, word, game_state, fm=True)
        curr_move.score = find_score(curr_move, game_state)
        first_moves.append(curr_move)
    return first_moves
                 

def find_intersection_moves(row: int, col: int, hand: str, game_state):
    intersection_moves = list()
    neighbors = find_neighbors(row, col, game_state)
    if(neighbors[2] or neighbors[3]): #vertical
        words = dictionary_searcher.get_all_words(hand + game_state.board[row][col].occupant, game_state.language)

        for word in words:
            curr_move = Move(True, row, col, word, game_state)
            if is_legal_move(curr_move, game_state):
                curr_move.score = find_score(curr_move, game_state)
                intersection_moves.append(curr_move)
    elif(neighbors[0] or neighbors[1]): #vertical
        words = dictionary_searcher.get_all_words(hand + game_state.board[row][col].occupant, game_state.language)

        for word in words:
            curr_move = Move(False, row, col, word, game_state)
            if is_legal_move(curr_move, game_state):
                curr_move.score = find_score(curr_move, game_state)
                intersection_moves.append(curr_move)

    return intersection_moves

def find_addition_moves(row: int, col: int, hand: str, game_state):
    neighbors = find_neighbors(row, col, game_state)
    substring = ""
    additon_moves = list()
    if neighbors[1] == True:
        displacement = 0
        while(row + displacement < len(game_state.board)  and not game_state.board[row + displacement][col].is_empty): #finds substring
            substring += game_state.board[row + displacement][col].occupant 
            displacement += 1
        words = dictionary_searcher.get_all_words_with_subset(substring, hand + substring, game_state.language)
        for word in words:
            curr_move = Move(True, row, col, word, game_state)
            if curr_move.word != substring and is_legal_move(curr_move, game_state): #makes sure that we are playing a new word nost just  and curr_move.word != substring
                curr_move.score = find_score(curr_move, game_state)
                additon_moves.append(curr_move)
    
    substring = ""
    if neighbors[3] == True:
        displacement = 0
        while(col + displacement < len(game_state.board) and not game_state.board[row][col + displacement].is_empty):
            substring += game_state.board[row][col + displacement].occupant 
            displacement += 1
        words = dictionary_searcher.get_all_words_with_subset(substring, hand + substring, game_state.language)
        for word in words:
            curr_move = Move(False, row, col, word, game_state)
            if curr_move.word != substring and is_legal_move(curr_move, game_state): #makes sure that we are playing a new word nost just  and curr_move.word != substring
                curr_move.score = find_score(curr_move, game_state)
                additon_moves.append(curr_move)

    return additon_moves
   
def find_adjacency_moves(words, row: int, col: int, hand: str, game_state):
    curr_move: Move
    adjacency_moves = list()
    for word in words:
        curr_move = Move(True, row, col, word, game_state)
        num_adjacent = 0
        for coord in curr_move.span:
            if coords_in_range(coord, game_state):
                num_adjacent += find_num_neighbors(coord[0], coord[1], game_state)
        if num_adjacent == 0: #not playable
            return adjacency_moves
        if(is_legal_move(curr_move, game_state)):
            curr_move.score = find_score(curr_move, game_state)
            adjacency_moves.append(curr_move)

        curr_move = Move(False, row, col, word, game_state)
        num_adjacent = 0
        for coord in curr_move.span:
            if coords_in_range(coord, game_state):
                num_adjacent += find_num_neighbors(coord[0], coord[1], game_state)
        if num_adjacent == 0: #not playable
            return adjacency_moves
        if(is_legal_move(curr_move, game_state)):
            curr_move.score = find_score(curr_move, game_state)
            adjacency_moves.append(curr_move)

    return adjacency_moves

def is_legal_move(move: Move, game_state: board_processor.Game_State):

    if(move == None):
        return False

    if not game_state.board[move.i][move.j].is_empty:
        return False

    if not dictionary_searcher.is_a_word(move.word, game_state.language): #may be redundant
        return False
    
    # if (coords_in_range((move.span[len(move.span) - 1][0] + 1, move.span[len(move.span) - 1][0] + 1), game_state)
    #     and not game_state.board[move.span[len(move.span) - 1][0] + 1][[len(move.span) - 1][1] + 1].is_empty): #!! need to implement last idx + 1 check 
    #     return False 

    idx = 0
    for coords in move.span:
        if (not coords_in_range(coords, game_state) 
            or ((not game_state.board[coords[0]][coords[1]].is_empty) and (game_state.board[coords[0]][coords[1]].occupant != move.word[idx]))):
            return False
        idx += 1
   
    if move.orientation == True: 
        if(move.span[0][0] - 1 >= 0 
           and not game_state.board[move.span[0][0] - 1][move.span[0][1]].is_empty): #up
            return False   
        if(move.span[len(move.span) - 1][0] + 1 < len(game_state.board)
           and not game_state.board[move.span[len(move.span) - 1][0] + 1][move.span[0][1]].is_empty): #down
            return False
        
    elif move.orientation == False: 
        if(move.span[0][1] - 1 >= 0
           and not game_state.board[move.span[0][0]][move.span[0][1] - 1].is_empty): #left
            return False   
        if(move.span[len(move.span) - 1][1] + 1 < len(game_state.board) 
           and not game_state.board[move.span[0][0]][move.span[len(move.span) - 1][1] + 1].is_empty): #right
            return False
    
    idx = 0

    intersecting_strings = get_intersecting_strings(move, game_state)
    for string in intersecting_strings:
        if len(string) != 1 and not dictionary_searcher.is_a_word(string, game_state.language):
            return False

    return True

def coords_in_range(coords: tuple, game_state) -> bool:
    if coords[0] < len(game_state.board) and coords[1] < len(game_state.board) and coords[0] >= 0 and coords[1] >= 0:
        return True
    else:
        return False

def find_score(move: Move, game_state: board_processor.Game_State):
    word_score = 0
    word_multi = 1
    intersection_score = 0
    #find the score of the word first
    for index in range(len(move.word)):
        curr_space = game_state.board[move.span[index][0]][move.span[index][1]]
        if curr_space.is_empty:
            word_score += score_lookup(move.word[index]) * curr_space.letter_multiplier
            word_multi *= curr_space.word_multiplier
        else:
            word_score += score_lookup(curr_space.occupant) 

    word_score *= word_multi

    interecting_strings = get_intersecting_strings(move, game_state)
    for index in range(len(move.word)):
       curr_space = game_state.board[move.span[index][0]][move.span[index][1]]
       if curr_space.is_empty and len(interecting_strings[index]) > 1:
           intersection_score += ((raw_word_score(interecting_strings[index]) 
                                  - score_lookup(move.word[index]) 
                                  + (score_lookup(move.word[index]) * curr_space.letter_multiplier)) 
                                  * curr_space.word_multiplier)

   
    return word_score + intersection_score

def get_intersecting_strings(move, game_state):
    strings = list()
    for coord in move.span:
        idx = 1
        string = move.word[move.span.index(coord)]
        if move.orientation:

            while (coords_in_range((coord[0], coord[1] - idx), game_state) and (coords_in_range((coord[0], coord[1] + idx), game_state)) 
                   and (not game_state.board[coord[0]][coord[1] + idx].is_empty or not game_state.board[coord[0]][coord[1] - idx].is_empty)):
                
                if not game_state.board[coord[0]][coord[1] + idx].is_empty:
                    string = string + game_state.board[coord[0]][coord[1] + idx].occupant 
                if not game_state.board[coord[0]][coord[1] - idx].is_empty:
                    string = game_state.board[coord[0]][coord[1] - idx].occupant + string
                idx += 1
            strings.append(string)

        elif not move.orientation:
            while (coords_in_range((coord[0] - idx, coord[1]), game_state) and (coords_in_range((coord[0] + idx, coord[1]), game_state))):                
                if not game_state.board[coord[0] + idx][coord[1]].is_empty:
                    string = string + game_state.board[coord[0] + idx][coord[1]].occupant
                if not game_state.board[coord[0] - idx][coord[1]].is_empty:
                    string = game_state.board[coord[0] - idx][coord[1]].occupant + string
                idx += 1
            strings.append(string)

    return strings

def find_intersection_index(move: Move, i: int, j: int, game_state: board_processor.Game_State) -> int:
    intersection_idx = move.word.index(game_state.board[i][j].occupant)
    return intersection_idx

def board_is_empty(board):
    return board[7][7].is_empty

# returns a list of boolean respesenting if there is a neighbor up down left or right of the given index respectively
def find_neighbors(i:int, j:int, game_state: board_processor.Game_State) -> list:
    neighbors: list = list() 
    neighbors.append(False)
    if i - 1 >= 0 and not game_state.board[i - 1][j].is_empty: 
        neighbors[0] = True
    neighbors.append(False)
    if i + 1  < len(game_state.board) and not game_state.board[i + 1][j].is_empty:
        neighbors[1] = True
    neighbors.append(False)
    if j + 1 >= 0 and not game_state.board[i][j - 1].is_empty:
        neighbors[2] = True
    neighbors.append(False)
    if j + 1 < len(game_state.board) and not game_state.board[i][j + 1].is_empty:
        neighbors[3] = True
    return neighbors

def find_neighbor(i:int, j:int, game_state: board_processor.Game_State) -> int:
    neighbors: list = list(bool) 
    neighbors[0] = False
    if i + 1 < len(game_state.board) and not game_state.board[i - 1][j].is_empty: 
        return 0
    if i - 1 >= 0 and not game_state.board[i + 1][j].is_empty:
        return 1
    neighbors[2] = False
    if j + 1 < len(game_state.board) and not game_state.board[i][j - 1].is_empty:
        return 2
    neighbors[3] = False
    if j - 1 >= 0 and not game_state.board[i][j + 1].is_empty:
        return 3
    return -1

def find_num_neighbors(i:int, j:int, game_state: board_processor.Game_State) -> int:
    num: int = 0
    if i + 1 < len(game_state.board) and not game_state.board[i + 1][j].is_empty:
        num += 1
    if i - 1 >= 0 and not game_state.board[i - 1][j].is_empty:
        num += 1
    if j + 1 < len(game_state.board) and not game_state.board[i][j + 1].is_empty:
        num += 1
    if j - 1 >= 0 and not game_state.board[i][j - 1].is_empty:
        num += 1
    return num

def find_neighbor_orientation(i:int, j:int, game_state: board_processor.Game_State) -> int:
    num: int = 0
    if i + 1 < len(game_state.board) and not game_state.board[i + 1][j].is_empty:
        num += 1
    if i - 1 >= 0 and not game_state.board[i - 1][j].is_empty:
        num += 1
    if j + 1 < len(game_state.board[0]) and not game_state.board[i][j + 1].is_empty:
        num -= 1
    if j - 1 >= 0 and not game_state.board[i][j - 1].is_empty:
        num -= 1
    return num

def raw_word_score(word:str) -> int:
    score:int = 0
    for letter in word: 
        score += score_lookup(letter) 
    return score

# TODO hardcoded for testing purposes need to refactor to work with other languages
def score_lookup(char:str) -> int:
    if char in ("a","e","i","o","u","l","n","r","s","t") or char.lower() in ("a","e","i","o","u","l","n","r","s","t"):
        return 1
    elif char in ("d","g") or char.lower() in ("d","g"):
        return 2
    elif char in ("b","c","m","p") or char.lower() in ("b","c","m","p"):
        return 3
    elif char in ("f","h","v","y","w") or char.lower() in ("f","h","v","y","w"):
        return 4
    elif char in ("k") or char.lower() in ("k"):
        return 5
    elif char in ("j","x") or char.lower() in ("j","x"):
        return 8
    elif char in ("q","z") or char.lower() in ("q","z"):
        return 10
    else: 
        return 0
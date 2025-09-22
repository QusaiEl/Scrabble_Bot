# @author Qusai Elwazir

import board_processor
import move_analyzer
import dictionary_processor
import dictionary_searcher

this_state = board_processor.get_board_from_list(
                                    [["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "F", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "F", "F", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "o", "O", "C", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "u", "L", "K", "", "", "D", "A", "D", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "O", "", "D", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "G", "", "A", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                     ["","", "", "", "", "", "", "", "", "", "", "", "", "", ""]])

# addition_moves = move_analyzer.find_addition_moves(6,7,"abcdefdgqweg", this_state)
# intersection_moves = move_analyzer.find_intersection_moves(6,4,"absdfaqqe",this_state)

# all_moves = move_analyzer.find_all_moves("aledse", this_state)

# for move in all_moves:
#     print(move.word)


#THERE ARE STILL MANY ISSUES FIX THEM!
max_move = move_analyzer.find_maximal_move("undraiser", this_state) #!! issue only playing cad 
print(str(max_move.word) +  " ["+ str(max_move.i) + "]" + "["+ str(max_move.j)+ "]" + str(max_move.score) + " " + str(max_move.orientation) + " intersecting at " + str(max_move.intersection))



for idx in range(len(max_move.word)):
    this_state.board[max_move.span[idx][0]][max_move.span[idx][1]].occupant = max_move.word[idx]



for i in range(len(this_state.board)):
    for j in range(len(this_state.board)):
        if(this_state.board[i][j].occupant == ""):
            print("0 ", end="")
        else:

            print(this_state.board[i][j].occupant + " ", end="")
    print(" ")
print("score: " + str(max_move.score))


# max_m = move_analyzer.Move(False, 4, 2, "you",this_state)
# print(move_analyzer.is_legal_move(max_m,this_state)
# print(move_analyzer.find_score(max_m, this_state))







# # move1 = move_analyzer.Move(False, 6,7,"OLPHA", this_state)
# move2 = move_analyzer.Move(False, 6,7,"Owner", this_state)#!! edge case  
# move3 = move_analyzer.Move(False, 6,8,"NOd", this_state)
# # move3 = move_analyzer.Move(False, 7,9,"NODS", this_state)
# # move3 = move_analyzer.Move(False, 7,7,"NODOLO", this_state)
# # print(move.start_idx)
# # print(move_analyzer.find_score(move1, this_state))
# print(move_analyzer.find_score(move2, this_state))
# print(move_analyzer.find_score(move3, this_state))
# # print(move_analyzer.find_score(move3, this_state))

# # print(move_analyzer.find_score(move3, this_state))

# # print(move_analyzer.is_legal_move(move1, this_state))
# print(move_analyzer.is_legal_move(move2, this_state))
# print(move_analyzer.is_legal_move(move3, this_state))
# # print(move_analyzer.is_legal_move(move3, this_state))

# print(move_analyzer.is_legal_move(move3, this_state))
#!!tests for board setup
# print(this_state.board[6][7].is_empty)
# print(this_state.board[6][7].occupant)
# print(this_state.board[7][7].is_empty)
# print(this_state.board[7][7].occupant)
#!! tests for score_lookup, calculate_score and find_orientation
# print(move_analyzer.score_lookup("a"))
# print(move_analyzer.calculate_score("abc"))
# print(move_analyzer.find_orientation(7,7,this_state))
# print(move_analyzer.find_orientation(6,7,this_state))
# print(move_analyzer.find_orientation(5,7,this_state))
# print(move_analyzer.find_orientation(4,7,this_state))
# print(move_analyzer.find_orientation(7,8,this_state))
# print(move_analyzer.find_orientation(7,9,this_state))
# print(move_analyzer.find_orientation(7,10,this_state))
# print(move_analyzer.find_orientation(5,5,this_state))
# print(move_analyzer.find_orientation(0,0,this_state))

# print(move_analyzer.find_num_neighbors(7,7,this_state))
# print(move_analyzer.find_num_neighbors(6,7,this_state))
# print(move_analyzer.find_num_neighbors(5,7,this_state))
# print(move_analyzer.find_num_neighbors(4,7,this_state))
# print(move_analyzer.find_num_neighbors(7,8,this_state))
# print(move_analyzer.find_num_neighbors(7,9,this_state))
# print(move_analyzer.find_num_neighbors(7,10,this_state))
# print(move_analyzer.find_num_neighbors(5,5,this_state))
# print(move_analyzer.find_num_neighbors(0,0,this_state))

#!! tests for get_all_neighboring_strings_with_scores
# print(move_analyzer.get_all_neighboring_strings_with_scores(7,8, "k", 6,8, this_state))
# print(move_analyzer.get_all_neighboring_strings_with_scores(7,8, "k", 8,8, this_state))

#!! tests for is_legal_move
# my_move0 = move_analyzer.Move(7,8, "Ysfqw",0, this_state)
# my_move1 = move_analyzer.Move(7,8, "asssss",0, this_state)
# my_move2 = move_analyzer.Move(7,8, "YU",0, this_state)
# my_move3 = move_analyzer.Move(7,8, "butt",0, this_state) ## FAILS CASE SENSITIFIY
# my_move4 = move_analyzer.Move(3,7, "SMELL",0, this_state)
# my_move5 = move_analyzer.Move(3,7, "SMEW",0, this_state)
# my_move6 = move_analyzer.Move(4,7, "DAL",0, this_state)
# my_move7 = move_analyzer.Move(1,1, "XIS",0, this_state)

# print("0 " + str(move_analyzer.is_legal_move(my_move0, this_state))) #TODO moves are case sensitive
# print("1 " + str(move_analyzer.is_legal_move(my_move1, this_state)))
# print("2 " + str(move_analyzer.is_legal_move(my_move2, this_state)))
# print("3 " + str(move_analyzer.is_legal_move(my_move3, this_state)))
# print("4 " + str(move_analyzer.is_legal_move(my_move4, this_state)))
# print("5 " + str(move_analyzer.is_legal_move(my_move5, this_state)))
# print("6 " + str(move_analyzer.is_legal_move(my_move6, this_state)))
# print("7 " + str(move_analyzer.is_legal_move(my_move7, this_state)))

#!! tests for get_all_moves
# l = move_analyzer.get_all_moves("abd", this_state)
# for move in l:
#     print("[" + str(move.i) + "]" + "[" + str(move.j)+ "]"  + str(move.word) + " scoring:" + str(move.score))

#!! tests for get_maximal_play
# hand = "abd"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print()
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) 
#       + " " + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index: " 
#       + str(best_move.intersection) 
#       + " with hand: " + hand )

# print()
# hand = "abcdefg"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) + " "
#        + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index: " 
#        + str(best_move.intersection)
#        + " with hand: " + hand )


#!!! hand limit in scrabble is 7, for hands over 7, this takes a very long time to compute the optimal word
# print() 
# hand = "abcdefghijklmnopqrstuv"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) + " "
#        + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index:" 
#        + str(best_move.intersection)
#        + "with hand: " + hand )


# print()
# hand = "ueagrjov"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) + " "
#        + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index: " 
#        + str(best_move.intersection)
#        + " with hand: " + hand)

# print()
# hand = "aeiou"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) + " "
#        + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index: " 
#        + str(best_move.intersection)
#        + " with hand: " + hand)
# print()
# hand = "o"
# best_move = move_analyzer.get_maximal_play(hand, this_state)
# print("[" + str(best_move.i) + "]" + "[" + str(best_move.j)+ "]"  + str(best_move.word) + " "
#        + best_move.dir + " scoring:" + str(best_move.score) + " intersecting with the island at word index: " 
#        + str(best_move.intersection)
#        + " with hand: " + hand)



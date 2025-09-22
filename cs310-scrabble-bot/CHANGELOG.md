
## Change Log
APR 27 2025 2:00pm - QUSAI ELWAZIR

- Added description of dictionary cleaning and search methodology.
- Added change log. 

APR 27 2025 6:00pm - QUSAI ELWAZIR

- Added dictionary processing class "dictionary_processor.py" that makes the dictionary easily and quickly searchable with sets of letters
- Added a dictionary searching class "dictionary_searcher.py" that searches a dictionary that has been processed by the dictionary processing class. This class is able to search a given dictionary via letter set, and is able to return boolean if a word is a word according to a dictionary or not.

APR 27 2025 7:00pm - QUSAI ELWAZIR
- Changed dictionary processing to create a 'language' tuple instead of needing to create a alphabet dict and a word dict outside the class. Now that is done inside the class so the scope of the class is more contained. Updated test classes to accomodate this change as well as updated params for "dictionary_searcher" class to take the new language tuple as a param for searching instead of taking 2 params of letter dict and word dict.

APR 27 2025 8:30pm - QUSAI ELWAZIR
- Started implementing gamestate analysis. Will need to refactor some of the dictionary searching code to accomodate finding the set of all playable words along with the set of all playable words for every subset of a given set of letters. Need to make letter scoring generic and according to dictionaries. Removed case sensitivity of dictionaries and alphabets. Updated readme method section start expressing the method by which we will be describing and assesing game-states.

APR 28 2025 11:50am - QUSAI ELWAZIR
- Added search function for the power set of a given set of letters. That is, A function that will output all possible words that can be made with a given set of letters. Implemented helper function that finds the power set of a set of letters. 

APR 28 2025 1:00pm - QUSAI ELWAZIR
- implemented schema for representing games states using two objects: space (a space on the board) and Game_State (containing information about the current game state including the board which is a matrix of Spaces). Implemented Score Calculator for a string of letters. Moved change log to its own file and out of the README md file.

APR 28 2025 2:00pm - QUSAI ELWAZIR
- Added helper functions: get_num_neighbors and get_orientation in the letter_checker to help with move legality analysis.
- Determined we will need to spit moves into two catagories: intersection, and fillspace. Intersection is the case when our move only intersects simply with the island(the blob of letters) n times where there are no other intersections of a different orientation. Fillspace is the case in which there are intersections in multiple orientations. Also started working on the first move case: simple intersection.
- 2:10pm note: IDEA, WHAT IF I JUST CHECK THE LEGALITY OF PLACING A WORD from the [i1][j1] to [i2][j2] by checking range and checking is_a_word on all immediate branches off of the word being placed

APR 28 2025 3:30pm - QUSAI ELWAZIR
- Added helper functions to help with new move assesment method. Also added stubs for future implementations related to move anaylisis.
- note: changed method by which we will be looking at move options. Instead of looking at moves as different types we will simply, for each of the letters in the word associated with the move, check if its neighbors, if there are any on the board, also form words. If they do not, then this word is not legal and will not be taken into account when choosing an optimal move. If all neighbors form words then each of the neighbors point value will be calculated and added to the score of the played word. This is the part of gamestate analyisis with the highest complexity since we will have to run "is_a_word", which runs in O(!n) time, on each possible each neighbor. 

APR 28 2025 5:00pm - QUSAI ELWAZIR
- added function that asseses the universal legality of playing a word on a set of tiles for any given state called is_legal_move which returns a tuple containing the the boolean value of the legality of the move and the point value of the move. This function relies on a helper function that was added called "get_all_neighboring_strings_with_scores" which returns a list of tuples containing all the strings that are adjacent to a given index. This helper function currently has an issue where it will not take into account words that pass through the index but only words that sprout off of the index. This function returns a tuple containing the list of all strings coming out of a given index with their respecive point values as the second index in the tuple.

APR 29 2025 5:00pm - QUSAI ELWAZIR
- tested all modules, and debugged current code. Reworked some of the anyalisis functions. Currently is functional but there is an issue with both how scores are calculated and with how created words that arent the chosen word are taken into account when scoring. I will fix these two issues tomorrow and then it should be fully functional.
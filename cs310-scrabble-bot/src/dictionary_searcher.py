# @author Qusai Elwazir

import dictionary_processor
from itertools import chain, combinations

#TODO implement search with blank tiles
#TODO IMPLEMENT SCORE CALC

# finds every possible word that can be made with a set of letters with given language tuple that is comprised of an alphabet and a dictionary
def get_all_words(letters: list, language: tuple) -> list:
    search_list = get_power_set(letters)
    word_list = list()
    temp = list()
    for sub_set in search_list: # searchs every subset and adds their respective words to the list
        temp = get_all_words_atlength(sub_set, language)
        if temp != "DNE": # ensure that we do not append lists of words that do not exist
           word_list += get_all_words_atlength(sub_set, language) # merge the new list
    return word_list

def get_all_words_with_subset(subset:str, letters: list, language: tuple):
    words = get_all_words(letters, language)
    words_with_subset = list()
    for word in words:
        if subset in word and not subset == word:
            words_with_subset.append(word)
    return words_with_subset

#takes a tuple list of #TODO
def get_all_words_with_fixed_indecies(letters: list, language: tuple):
    return

# searches a given dictionary with its respective alphabet using a list of letters and returns a list of all words that are 
# comprised of those letters and that are the same length as the list param "letters"
def get_all_words_atlength(letters: list, language: tuple) -> list:
    product = 1
    clean_letter = ""
    for letter in letters:
        clean_letter = letter.lower() # eliminates case sensitivity
        product *= language[0][clean_letter] # language[0] is the alphabet of the given language
    if not product in language[1]:
        return "DNE" ## case where there is no such word for a given set of letters
    return language[1][product]

# returns a list representation of the powerset of a given set of letters
# runs in O()
def get_power_set(letters: list) -> list:
    power_list = list(chain.from_iterable(combinations(letters, i) for i in range(len(letters)+1)))
    power_list.remove(())
    return power_list


# searches a given word with a given dictionary with its respective alphabet and returns if the given word is a word
# according to the alphabet and dictionary
def is_a_word(word: list, language: tuple) -> bool:
    sub_dictionary = get_all_words_atlength(word, language)
    clean_word = word.lower() # eliminates case sensitivity
    clean_words = "" 
    if(sub_dictionary == "DNE"):
        return False
    for words in sub_dictionary:
        clean_words = words.lower() # eliminates case sensitivity
        if(clean_word == clean_words):
            return True
    return False
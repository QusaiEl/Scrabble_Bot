# @author Qusai Elwazir

import dictionary_processor
import dictionary_searcher

language = dictionary_processor.create_language("Dictionary_Source/alphabet.txt", "Dictionary_Source/dictionary.txt")

# words = dictionary_searcher.get_all_words_atlength(["E", "T", "A", "L", "E"], language)
# for word in words:
#     print(word)
# words = dictionary_searcher.get_all_words_atlength(["B", "O", "O", "B"], language)
# for word in words:
#     print(word)

# print("for is_a_word = dictionary_searcher.search_dictionary_for_word(FALLENDIST, language)")
# is_a_word = dictionary_searcher.search_dictionary_for_word("FALlENDIST", language)
# print(is_a_word)
# print("for is_a_word = dictionary_searcher.search_dictionary_for_word(SLINKY, language)")
# is_a_word = dictionary_searcher.search_dictionary_for_word("SLINKY", language)
# print(is_a_word)
# print("for is_a_word = dictionary_searcher.search_dictionary_for_word(POWER, language)")
# is_a_word = dictionary_searcher.search_dictionary_for_word("PoWER", language)
# print(is_a_word)
# print("for is_a_word = dictionary_searcher.search_dictionary_for_word(FARTS, language)")
# is_a_word = dictionary_searcher.search_dictionary_for_word("FArTS", language)
# print(is_a_word)
# print("for is_a_word = dictionary_searcher.search_dictionary_for_word(APPARATUS, language)")
# is_a_word = dictionary_searcher.search_dictionary_for_word("APPARaTUS", language)
# print(is_a_word)
# print(dictionary_searcher.get_all_words("abcdef", language))
# is_a_word = dictionary_searcher.search_dictionary_for_word("ae", language)
# print(is_a_word)

word = "booties"
is_a_word = dictionary_searcher.is_a_word(word, language)
print(word + " " + str(is_a_word))
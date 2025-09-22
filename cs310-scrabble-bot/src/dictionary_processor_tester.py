# @author Qusai Elwazir

import dictionary_processor

language = dictionary_processor.create_language("Dictionary_Source/alphabet.txt", "Dictionary_Source/dictionary.txt")
for key, value in language[1].items():
    val = ""
    for element in value:
        val += element + ", "
    print(f"{key}: {val}")

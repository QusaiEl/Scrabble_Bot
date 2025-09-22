# @author Qusai Elwazir

#TODO IMPLEMENT SCORE ASSOC WITH ALPHEBET
# creates a tuple that contains the alphabet prime number relationships at index 0 and the processed dictionary associated with
# that alphabet at index 1
# neither are case sensitive
def create_language(alphabet_file, dictionary_file) -> tuple:
    alphabet = create_letter_dictionary(alphabet_file)
    dictionary = create_dictionary(dictionary_file, alphabet)
    return (alphabet, dictionary)

# @param file is the given dictionary that uses letters_dict which contains the alphebet that is relevant to the given dictionary that 
# we will be processing into a searchable structure the dictionary must be in the following format:
# each entry in the dictionary must be followed by a return character '\r' 
# This function returns a dict dictionary that contains prime products as keys and lists of words whos set of contained letters associated 
# prime numbers multiply to they key product.
# NOT CASE SENSITIVE
def create_dictionary(file, letter_dict: dict) -> dict:
    dictionary = dict()
    product = 1
    file = open(file, "r")
    for line in file: # for each word in the dictionary will update its key value to be 
        line = line[:-1]
        clean_line = line.lower() # eliminates case sensitivity
        for character in clean_line: # finds the product of the prime numbers associted with each letter in the word
            product *= letter_dict[character]
        if(not product in dictionary): # it is a new key we will instantiate a list to hold the words that contain this set of letters
            dictionary[product] = list()
        dictionary[product].append(clean_line)
        product = 1
    file.close()
    return dictionary

# populates the letter_map dictionary according to a given alphebet for a dicitonary. (useful for other languages scrabble)
# NOT CASE SENSITIVE
def create_letter_dictionary(file) -> dict:
    letter_map = dict()
    curr_prime = 2
    file = open(file, "r")
    clean_line = ""
    for line in file:
        clean_line = line.lower() # eliminates case sensitivity
        letter_map[clean_line[0]] = curr_prime
        curr_prime = next_prime(curr_prime)
    file.close()
    return letter_map
    

# finds the next prime number after a given integer.
def next_prime(curr_prime: int) -> int:
    next_number = curr_prime + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

# determines if a number is prime. Returns true if is prime and false if is not prime.
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int((num / 2) + 1)):
        if num % i == 0:
            return False
    return True


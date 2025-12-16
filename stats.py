import sys

def sort_on(items):
    return items["num"]

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()

    return file_contents
    
def get_letter_count(file_contents):
    book_text = get_book_text(sys.argv[1])
    book_words = book_text.split()
    alphabet_one_string = "abcdefghijklmnopqrstuvwxyz"

    alphabet = []
    for i in alphabet_one_string:
        alphabet.append(i)

    letter_list = []
    for character in alphabet:
        letter_count = {}
        count = 0
        for word in book_words:
            for letter in word:
                letter = letter.lower()
                if letter == character:
                    count += 1
                else:
                    pass
        letter_count["char"] = character
        letter_count["num"] = count
        letter_list.append(letter_count)
    letter_list.sort(reverse=True, key=sort_on)
    letters = [d["char"] for d in letter_list]
    num = [d["num"] for d in letter_list]
    char_count = [letters,num]
    
    return char_count
    

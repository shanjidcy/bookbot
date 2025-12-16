from stats import get_book_text, get_letter_count, sort_on
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pass

    book_text = get_book_text(sys.argv[1])
    book_text_list = book_text.split()
    word_count = len(book_text_list)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print("Found",word_count,"total words")
    print("--------- Character Count -------")
    char_count = get_letter_count(sys.argv[1])
    for n in range(0,26):
        print(f"{char_count[0][n]}: {char_count[1][n]}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
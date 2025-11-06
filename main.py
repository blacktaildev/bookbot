from stats import get_num_words
from stats import get_num_char
from stats import sort_char
import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print("============ BOOKBOT ============")
print(f'Analyzing book found at {sys.argv[1]}...')

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words.")

    print("--------- Character Count -------")
    char_count = get_num_char(book_text)
    sorted_char = sort_char(char_count)
    for item in sorted_char:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()
import sys
from stats import * 

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv)<2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    word_count = get_word_count(book_content)
    character_dict = get_char_count(book_content)
    sorted_dict_list = get_sorted_dictionary_list(character_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")
    
main()
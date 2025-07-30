def get_word_count(book_content):
    word_list = book_content.split()
    count = 0
    for word in word_list:
        count += 1
    return count

def get_char_count(book_content):
    char_dict = {}
    for char in book_content:
        char = char.lower()
        if char in char_dict: char_dict[char] += 1
        else: char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item["count"]

def get_sorted_dictionary_list(char_dict):
    dictionary_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            dictionary_list.append({"char": char, "count": count})
    dictionary_list.sort(key=sort_on, reverse=True)
    return dictionary_list
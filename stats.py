def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_num_char(book_text):
    char_count ={}
    for char in book_text:
        lower_case_char = char.lower()
        if lower_case_char in char_count:
            char_count[lower_case_char] += 1
        else:
            char_count[lower_case_char] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_char(char_count):
    char_list = []
    for c in char_count:
        new_char = {"char": c, "num": char_count[c]}
        char_list.append(new_char)  
    char_list.sort(reverse=True, key=sort_on)
    return char_list
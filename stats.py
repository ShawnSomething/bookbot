def get_book_text(file):
    with open(file) as file:
        file_contents = file.read()
        return file_contents

def count_words(file):
    text = get_book_text(file)
    num_words = 0
    for i in text.split():
        num_words += 1
    return print(f"Found {num_words} total words")

def count_characters(file):
    text = get_book_text(file)
    lower_case = text.lower()
    char_dict = {}
    for i in lower_case:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorts(file):
    character_dict = count_characters(file)
    new_list = []
    for i in character_dict:
         if i.isalpha():
            new_list.append({"char": i, "num": character_dict[i]})

    sorted_new_list = sorted(new_list, key=sort_on, reverse=True)

    for item in sorted_new_list:
        print(f"{item['char']}: {item['num']}")


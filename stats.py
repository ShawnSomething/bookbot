def get_book_text(file):
    with open(file) as file:
        file_contents = file.read()
    
    num_words = 0
    for i in file_contents.split():
        num_words += 1
    return print(f"{num_words} words found in the document")

def count_characters(file):
    with open(file) as file:
        file_contents = file.read()
    
    lower_case = file_contents.lower()
    char_dict = {}
    for i in lower_case:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    
    print(char_dict)
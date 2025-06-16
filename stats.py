def get_book_text(file):
    with open(file) as file:
        file_contents = file.read()
    num_words = 0
    for i in file_contents.split():
        num_words += 1
    return print(f"{num_words} words found in the document")
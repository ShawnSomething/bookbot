def get_book_text(file):
    with open(file) as file:
        file_contents = file.read()
    return print(file_contents)

def main():
    get_book_text("books/frankenstein.txt")


main()
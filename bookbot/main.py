import sys

from stats import word_count, char_count, sort_char_map


def get_book_text(fpath: str) -> str:
    file_contents = None

    with open(fpath, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents


def print_report(book_path) -> str:
    book_text = get_book_text(book_path)
    words = word_count(book_text)
    char_map = char_count(book_text)
    sorted_chars = sort_char_map(char_map)

    print(f"Found {words} total words")

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")

    for elem in sorted_chars:
        elem_char = elem["char"]
        elem_count = elem["num"]

        if elem_char.isalpha():
            print(f"{elem_char}: {elem_count}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    book_relative_path = sys.argv[1]
    print_report(book_relative_path)


if __name__ == "__main__":
    main()

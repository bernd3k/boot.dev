def word_count(book_text: str) -> int:
    """
    counts the words

    :param book_text: a text to count
    :type book_text: str
    :return: number of words
    :rtype: int
    """
    wc = 0

    wc += len(book_text.split())

    return wc


def char_count(book_text: str) -> dict[str, int]:
    """
    count individual characters in text

    :param book_text: Description
    :type book_text: str
    :return: Description
    :rtype: dict[str, int]
    """
    lower_case_text = book_text.lower()
    char_dict = {}

    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_char_map(character_count: dict[str, int]) -> list[dict[str, int]]:
    char_list = []

    for single_char in character_count:
        char_list.append(
            {
                "char": single_char,
                "num": character_count[single_char],
            }
        )

    return sorted(char_list, key=lambda x: x["num"], reverse=True)

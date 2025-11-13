def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def word_counter(text):
    words = text.split()
    return len(words)


def char_counter(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts


def sort_char_counts(char_dict):
    char_list = [{"char": c, "num": n} for c, n in char_dict.items()]

    def sort_on(item):
        return item["num"]

    char_list.sort(key=sort_on, reverse=True)
    return char_list

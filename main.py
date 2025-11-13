import sys
from stats import get_book_text, word_counter, char_counter, sort_char_counts
print("Usage: python3 main.py <path_to_book>")

def main():
    path = sys.argv[1]
    text = get_book_text(path)

    total_words = word_counter(text)
    char_counts = char_counter(text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()

print(sys.argv)

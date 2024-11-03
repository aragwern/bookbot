import sys

def open_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def read_book(file_path):
    file_contents = open_book(file_path)
    print(file_contents)


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars and char.isalpha():
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    return chars


def sort_char_count(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "count": char_dict[key]})
    return char_list

def report(file_path):
    text = open_book(file_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    char_count_list = sort_char_count(char_count)
    char_count_list.sort(reverse=True,key=lambda d: d["count"])
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("") # one empty line
    for entry in char_count_list:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")


def main(file_path):
    report(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)

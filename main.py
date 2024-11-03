def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for word in words:
            count += 1
    return count

def main():
    #read_book(r"books/frankenstein.txt")
    print(count_words(r"books/frankenstein.txt"))

main()

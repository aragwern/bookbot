def main():
    with open(r"books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
main()

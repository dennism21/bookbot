def main():
    path_to_file =  "./books/frankenstein.txt"
    text = read_book(path_to_file)
    words = count_words(text)
    letters = count_letters(text)
    report = generate_report(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for char in report:
        print(char)
    print("--- End report ---")


def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for c in text:
        c = c.lower()
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def generate_report(dict):
    sorted_dict = sorted(dict.items())
    new_list = []
    for k, v in sorted_dict:
        if k.isalpha():
            new_list.append(f"The {k} character was found {v} times")
    return new_list



main()

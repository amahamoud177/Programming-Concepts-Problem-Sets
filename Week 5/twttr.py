def main():
    word = input("Enter a word: ")
    print(shorten(word))

def shorten(word):
    for letter in word:
        if letter in "AEIOUaeiou":
            word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
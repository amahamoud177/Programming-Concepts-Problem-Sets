def main():
    shorten = input("Enter a word: ")
    for letter in shorten:
        if letter in "AEIOUaeiou":
            shorten = shorten.replace(letter, "")
    print(shorten)

if __name__ == "__main__":
    main()
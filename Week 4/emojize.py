from emoji import emojize

def main():
    input_codes = input("Enter an emoji code: ")
    print(emojize(input_codes, language='alias'))

if __name__ == "__main__":
    main()
def convert(smile, frown):
    smile = smile.replace(":)", "🙂")
    frown = frown.replace(":(", "🙁")
    return smile, frown

def main():
    smile_input = input("Enter a smiley face: ")
    frown_input = input("Enter a frowning face: ")
    smile, frown = convert(smile_input, frown_input)
    print(smile)
    print(frown)

main()
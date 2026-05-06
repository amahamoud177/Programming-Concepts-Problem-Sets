from validator_collection import validators, checkers, errors


def main():
    email_address = input("What is your email? ")
    check_email = checkers.is_email(email_address)
    if check_email:
        print("Valid")
    else:
        print("Invalid")




if __name__ == "__main__":
    main()

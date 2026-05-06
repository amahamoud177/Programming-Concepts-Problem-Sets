import random

def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0
        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
    if attempts == 3:
        print(f"The correct answer is {answer}")
    print(f"Your score is {score}")
    

        


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 100)
    else:
        return random.randint(1, 1000)
    



if __name__ == "__main__":
    main()


  
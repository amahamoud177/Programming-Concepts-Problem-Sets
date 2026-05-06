def main():
    while True:
        try:
            fuel = input("Enter a fraction: ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)
            if x < 0 or y < 0:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percentage = (x / y) * 100
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage:.0f}%")
            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
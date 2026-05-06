def main():
    while True:
        try:
            fuel = input("Enter a fraction: ")
            percentage = convert(fuel)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(function):
    x, y = function.split("/")
    x = int(x)
    y = int(y)
    if x < 0 or y < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = (x / y) * 100
    return round(percentage)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    

if __name__ == "__main__":
    main()
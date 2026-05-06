def main():

    expression = input("Enter an expression: ")

    x, y, z = expression.split()

    x = float(x)
    z = float(z)


    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    elif y == "/":
        answer = x / z
    else:
        print("Invalid operator")
        return
    print(f"{answer:.1f}")


if __name__ == "__main__":
    main()
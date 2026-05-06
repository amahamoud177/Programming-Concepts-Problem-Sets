def main():
    change = 50
    while change > 0:
        print(f"Amount due: {change}")
        try:
            coin = int(input("Insert a coin: "))
            if coin == 50 or coin == 25 or coin == 10 or coin == 5:
                change -= coin
            else:
                print("Invalid coin")
        except ValueError:
            continue
    print(f"Change owed: {change}")
    

if __name__ == "__main__":
    main()
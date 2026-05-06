def main():
    grocery_list = {}
    try:
       while True: 
        item_list = input("Enter the items in your grocery list: ")
        item_list = item_list.lower()
        if item_list in grocery_list:
            grocery_list[item_list] += 1
        else:
            grocery_list[item_list] = 1
    except EOFError:
        for item in sorted(grocery_list):
            print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
    
        

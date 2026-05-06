import inflect
p = inflect.engine()


def main():
    store_names = []
    try:
        while True:
            name = input("Name: ")
            store_names.append(name)
    except EOFError:
        joined_names = p.join(store_names)
        print(f"Adieu, adieu, to {joined_names}")
    
if __name__ == "__main__":
    main()


        

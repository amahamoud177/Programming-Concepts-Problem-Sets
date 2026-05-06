import sys

def main():
    if (len(sys.argv) != 2):
        print("Invalid usage")
        sys.exit(1)
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(filename) as f:
            lines = f.readlines()
            line_count = 0
            for line in lines:
                if line.strip() == "" or line.lstrip().startswith("#"):
                    continue
                else:
                    line_count += 1
            print(line_count)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()



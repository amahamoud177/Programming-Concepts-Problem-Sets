import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py .csv file")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            table = []
            for row in reader:
                table.append(row)
        print(tabulate(table, headers = "firstrow", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
            
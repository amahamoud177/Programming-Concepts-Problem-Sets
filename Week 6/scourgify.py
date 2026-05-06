import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv ")
    before_file = sys.argv[1]
    after_file = sys.argv[2]
    if not before_file.endswith(".csv") or not after_file.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(before_file) as before:
            reader = csv.reader(before)
            next(reader)
            with open(after_file, "w") as after:
                writer = csv.writer(after)
                writer.writerow(["first", "last", "house"])
                for row in reader:
                    last, first = row[0].split(",")
                    first = first.strip()
                    last = last.strip()
                    writer.writerow([first, last, row[1]])
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_search = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(um_search)
    







if __name__ == "__main__":
    main()
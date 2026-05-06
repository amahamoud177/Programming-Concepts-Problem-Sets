import re
import sys


def main():
    ip = validate(input("IPv4 Address: "))
    print(ip)


def validate(ip):
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    for num in ip:
        if not num.isdigit():
            return False
        if num[0] == "0" and len(num) > 1:
            return False
        num = int(num)
        if num < 0 or num > 255:
            return False
    else:
        return True



if __name__ == "__main__":
    main()
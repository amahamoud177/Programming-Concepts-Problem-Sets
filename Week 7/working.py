import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"^([1-9]|1[0-2])(?::(0[0-9]|[1-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::(0[0-9]|[1-5][0-9]))? (AM|PM)$",s)
    if time is None:
        raise ValueError("Invalid time format")
    start_hour = int(time.group(1))
    start_mins = time.group(2)
    start_meridiem = time.group(3)
    end_hour = int(time.group(4))
    end_mins = time.group(5)
    end_meridiem = time.group(6)
    if start_meridiem == "PM" and start_hour != 12:
        start_hour = start_hour + 12
    if end_meridiem == "PM" and end_hour != 12:
        end_hour = end_hour + 12
    if start_meridiem == "AM" and start_hour == 12:
        start_hour = 0
    if end_meridiem == "AM" and end_hour == 12:
        end_hour = 0
    if start_mins is None:
        start_mins = "00"
    if end_mins is None:
        end_mins = "00"
    return f"{start_hour:02d}:{start_mins} to {end_hour:02d}:{end_mins}"

    





if __name__ == "__main__":
    main()
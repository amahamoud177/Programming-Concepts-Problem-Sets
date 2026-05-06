def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if (month < 1 or month > 12) or (day < 1 or day > 31):
                    continue
                print(f"{year}-{month:02d}-{day:02d}")
                break
            elif "," in date:
                words = date.split(",")
                date_split = words[0].strip().split()
                month = date_split[0]
                day = date_split[1]
                year = words[1].strip()
                if month in months:
                    month_num = months.index(month) + 1
                    day = int(day)
                    year = int(year)
                    if day < 1 or day > 31:
                        continue
                    print(f"{year}-{month_num:02d}-{day:02d}")
                break
            else:
                continue
        except:
            continue



if __name__ == "__main__":
    main()

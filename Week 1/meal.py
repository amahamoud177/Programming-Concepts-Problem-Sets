def main():
    meal_time = input("What time is it? ")
    converted_time = convert(meal_time)
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")




def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes
    


if __name__ == "__main__":
    main()
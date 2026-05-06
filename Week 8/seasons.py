from datetime import date
import inflect
import sys

p = inflect.engine()



def main():
    try:
        birth_date = input("What is your birthday? ")
        birth_date = date.fromisoformat(birth_date)
        minutes_lived = calculate_minutes(birth_date)
        minutes_converted = p.number_to_words(minutes_lived)
        converted_words = minutes_converted.replace(" and ", " ")
        print(converted_words)
    except ValueError:
        sys.exit("Invalid date")
    
    

def calculate_minutes(birth_date):
    today_date = date.today()
    date_difference = today_date - birth_date
    days = date_difference.days
    minutes = days * 1440
    return minutes


    



if __name__ == "__main__":
    main()
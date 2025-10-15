import datetime


def num_input_validation(user_input):
    while user_input.isnumeric() == False or user_input == "":
        user_input = input("Error, this input is invalid, Please try again: ")
    print("Thank you, your input has been validated.")

    return int(user_input)


def main():
    print("Welcome to the age calculating machine.")
    birth_year = input("Please input the year you were born, e.g. '2001': ")
    birth_year = num_input_validation(birth_year)
    birth_month = input("Please input the month you were born, e.g. '09' for September: ")
    birth_month = num_input_validation(birth_month)
    birth_day = input("Please input the day you were born, e.g. '21' for the 21st: ")
    birth_day = num_input_validation(birth_day)

    today = datetime.date.today()
    birthday_date = datetime.date(birth_year, birth_month, birth_day)
    years_delta = today.year - birthday_date.year
    months_delta = today.month - birthday_date.month
    days_delta = today.day - birthday_date.day

    print(f"Your Age is: {years_delta} years, {months_delta} months and {days_delta} days old" )



main()



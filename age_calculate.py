from datetime import date

year = int(input("Enter Birth Year (YYYY): "))
month = int(input("Enter Birth Month (MM): "))
day = int(input("Enter Birth Day: "))

birth_date = date(year, month, day)
today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"{age} years old. ")
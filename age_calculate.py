from datetime import date

# Input birth date
year = int(input("Enter Birth Year (YYYY): "))
month = int(input("Enter Birth Month (MM): "))
day = int(input("Enter Birth Day: "))

birth_date = date(year, month, day)
today = date.today()

# Calculate age in years
age_years = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

# Calculate the most recent birthday
last_birthday = date(today.year, birth_date.month, birth_date.day)
if last_birthday > today:
    last_birthday = date(today.year - 1, birth_date.month, birth_date.day)

# Days since last birthday
age_days = (today - last_birthday).days

print(f"{age_years} years and {age_days} days old.")

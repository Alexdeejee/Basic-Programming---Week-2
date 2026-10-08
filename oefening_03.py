# Exercise 03
from datetime import datetime

birth_year = int(input("What is your year of birth? "))
birth_month = int(input("What month were you born? "))
now = datetime.now()

if birth_month < 1 or birth_month > 12:
    print("Unknown month.")
elif (birth_year, birth_month) > (now.year, now.month):
    print("The birth date cannot be in the future.")
else:
    age = now.year - birth_year
    if now.month < birth_month:
        age -= 1
    if age >= 18:
        print("You are 18 or older.")
    else:
        print("You are under 18.")
# Zonder geboortedag is dit een controle op maandniveau.
# De alcoholuitspraak uit de bundel wordt hier niet als juridische regel gebruikt.

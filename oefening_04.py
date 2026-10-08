# Exercise 04
# De bundel geeft regels voor 0, 2 en >2, maar niet voor 1 jaar.
# Daarom verzinnen we voor 1 jaar geen omzetting.
age = int(input("What is your dog's age? "))
if age < 0:
    print("Error: age cannot be negative.")
elif age == 0:
    print("This age is equivalent to 14 years in human years.")
elif age == 1:
    print("The assignment does not specify a conversion for 1 year.")
elif age == 2:
    print("This age is equivalent to 22 years in human years.")
else:
    human_age = 22 + (age - 2) * 5
    print(f"This age is equivalent to {human_age} years in human years.")

# Exercise 13
def give_celsius(t_in_fahrenheit: float) -> float:
    return (t_in_fahrenheit - 32) * 5 / 9


def give_fahrenheit(t_in_celsius: float) -> float:
    return t_in_celsius * 9 / 5 + 32


unit = input("Which temperature unit do you use? [C: Celsius, F: Fahrenheit] ").upper()
if unit == "C":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = give_fahrenheit(temperature)
    print(f"The corresponding temperature in Fahrenheit is {result:.2f}")
elif unit == "F":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = give_celsius(temperature)
    print(f"The corresponding temperature in Celsius is {result:.2f}")
else:
    print("Unknown temperature unit. Choose C or F.")

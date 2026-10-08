# Exercise 11
def give_max(number1: float, number2: float, number3: float) -> float:
    maximum = number1
    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    return maximum


print(give_max(4, 9, 2))       # 9
print(give_max(8, 3, 12))      # 12
print(give_max(-5, -2, -8))    # -2
print(give_max(7, 7, 3))       # 7

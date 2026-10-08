# Exercise 05
from math import ceil, floor

score = float(input("Enter your score: "))
if score < 0 or score > 20:
    print("Error: enter a score between 0 and 20.")
else:
    decimal_part = score - floor(score)
    if decimal_part < 0.5:
        rounded_score = floor(score)
    else:
        rounded_score = ceil(score)
    if rounded_score >= 10:
        print(f"Congratulations, you passed! Your score is: {rounded_score}.")
    else:
        print(f"Alas, better luck next time! Your score is: {rounded_score}.")

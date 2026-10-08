# Homework 3
# De bundel wisselt namen; we gebruiken consequent get_message.
def get_message(hour: int, firstname: str) -> str:
    if hour < 0 or hour > 23:
        return "Unknown hour. Choose a value between 0 and 23."
    elif 7 <= hour < 12:
        return f"Good morning, {firstname}."
    elif hour == 12:
        return f"Yay, it's afternoon, {firstname}."
    elif 13 <= hour < 17:
        return f"Good afternoon, {firstname}."
    elif 17 <= hour < 21:
        return f"Good evening, {firstname}."
    else:
        return f"Good night, {firstname}."


hour = int(input("What time is it? "))
firstname = input("What is your first name? ")
welcome = get_message(hour, firstname)
print(welcome)

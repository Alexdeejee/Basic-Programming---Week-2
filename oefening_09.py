# Exercise 09
def create_welcome_in_class(name: str, class_group: str = "1CTAI") -> str:
    return f"Welcome {name} in {class_group}!"


name = input("What is your first name? ")
class_group = input("What is your class group? ")
message = create_welcome_in_class(name, class_group)
print(message)


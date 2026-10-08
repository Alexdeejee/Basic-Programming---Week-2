# Exercise 10
def calculate_result(a: float, b: float, c: float = 0, d: float = 0) -> float:
    return a - b + c - d


print(calculate_result(10, 3, 5, 2))                 # 10
print(calculate_result(d=2, c=5, b=3, a=10))        # 10
print(calculate_result(10, 3))                     # 7

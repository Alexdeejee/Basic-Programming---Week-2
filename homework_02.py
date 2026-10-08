# Homework 2
def exclusive_to_include(amount: float, vat_percentage: float) -> float:
    return amount * (1 + vat_percentage / 100)


excl_vat = float(input("What is the amount excluding VAT? "))
vat_percentage = float(input("What is the percentage of VAT? "))
incl_vat = exclusive_to_include(excl_vat, vat_percentage)
print(f"The inclusive amount you have to pay is: {incl_vat}")

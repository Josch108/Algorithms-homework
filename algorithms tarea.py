def division (number):
    if number % 3 == 0 and number % 2 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if division (number):
    print(f"{number} is divisible by both 3 and 2.")
else:
    print(f"{number} is not divisible by both 3 and 2.")

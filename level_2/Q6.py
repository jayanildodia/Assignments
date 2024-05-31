# Write a Python program to check if a number is a power of twousing recursion.

def poweroftwo(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    elif n % 2 == 0:
        return poweroftwo(n // 2)
    else:
        return False

number = int(input("Enter a number: "))
if poweroftwo(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")

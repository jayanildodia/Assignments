# Write a Python program to calculate the LCM (Least CommonMultiple) of two numbers.
# number1 = 12, number2 = 18
# LCM of 12 and 18 are: 36

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
result = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {result}")

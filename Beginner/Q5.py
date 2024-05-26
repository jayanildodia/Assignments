#Write a Python program to find the factorial of a number using a for loop.

x = int(input("Enter the number you want a factorial of: "))
fact = 1

for i in range(1, x+1, 1):
    fact = fact*i

print("factorial of given number is ", fact)

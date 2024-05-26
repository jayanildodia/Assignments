# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as astring
# If a number is divisible by 5 it should print “Python Training” asa string
# If a number is divisible by both 3 and 5 it should print“Consultadd - Python Training” as a string.

x = int(input("Enter a number:"))

if x%3 == 0 and x%5 == 0: #If divisible by both 3 and 5
    print("Consultadd - Python Training")
elif x%3 == 0: #If divisible by just 3
    print("Consultadd")
elif x%5 == 0: #If divisible by just 5
    print("Python Training")
else:
    pass

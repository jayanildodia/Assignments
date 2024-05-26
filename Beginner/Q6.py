# Write a Python program to check if a given number is a perfect number.
# A Perfect number is a positive integer that is equal to the sum ofits proper divisors.
# For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +3 = 6, so 6 is a perfect number.
# Input: 5
# Output: No

x = int(input("Enter the number you want to work with: "))
multi = 1
add = 0
for i in range(1, x+1, 1):
    for j in range(1, i+1, 1):
        add = add + j
        multi = multi * j
        if add == multi:
            print("{} is a perfect number!" .format(x))
            break

# Write a program that accepts a string as input from the user andcalculates the number of digits and letters.
# Input: Hello123
# Output: Alphabets: 5 & Number : 3

x = input("Enter a string of Alphanumeric Characters:")
int_count = 0
alp_count = 0
for i in x:
    if i.isdigit():
        int_count += 1
    elif i.isalpha():
        alp_count += 1
    else:
        pass
print("Alphabets: {} & Number: {}" .format(alp_count, int_count))

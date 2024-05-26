# Write a Python program to calculate the sum of digits of a givennumber until the sum becomes a single-digit number.
# Sample Input: num = 987
# Sample Output: Sum_of_digits = 24,
# Again compute the sum of digits so that it can be reduced to one single digit.
# Final Output: 6

x = list(input())
lenx = len(x)
while lenx != 1:
    sum = 0
    for i in x:
        sum = sum + (int(i))
    sumx = str(sum)
    x = list(sumx)
    lenx = len(x)
print(sum)

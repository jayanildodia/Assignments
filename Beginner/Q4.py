# Write a Python program to find the sum of all odd numbersbetween two given numbers.
# Start = 1, stop = 10
# Sum of odd numbers: 25

start_num = int(input("Give the Starting odd number: "))
end_num = int(input("Give Ending odd number: "))
sum = 0

if start_num%2 == 1:
    for x in range(start_num, end_num+1, 2):
        sum = sum + x
else:
    for x in range(start_num+1, end_num+1, 2):
        sum = sum + x

print("Sum of all odd numbers between {} and {} is {}" .format(start_num, end_num, sum))

# Write a Python function that finds the median of a list ofnumbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.0

def medianofnums(numbers):
    sortednums = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        median = sortednums[n // 2]
    else:
        middle1 = sortednums[n // 2 - 1]
        middle2 = sortednums[n // 2]
        median = (middle1 + middle2) / 2
    return median

numbers = input("Temperature data input here with spaces: ").split()
numbers = [int(x) for x in numbers]

medianvalue = medianofnums(numbers)
print(f"The median of {numbers} is {medianvalue}")

# Given an array of N integers and an integer K, find the number ofpairs of elements
# in the array whose sum is equal to K.
# Sample Input: arr = [1, 2, 3, 4, 5], k = 6
# Sample Output: Pair count: 2

arr = input("Enter the list of numbers using spaces:")
arr = arr.split()
arr = [int(i) for i in arr]
k = int(input("Enter an integer you want the sum to be equal to: "))
count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            count += 1
        else:
            continue
print(count)

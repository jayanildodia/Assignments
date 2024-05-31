# Create a function that takes a list and returns a new list with unique elements of the first list.
# Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
# Sample Output: list2 = [1, 2, 3, 4, 5]

x = input("Enter the list of numbers using spaces:")
x = x.split()
x = [int(i) for i in x]
x.sort()
newlist = []

for i in range(len(x)):
    if i == 0 or x[i] != x[i-1]:
        newlist.append(x[i])

print(newlist)

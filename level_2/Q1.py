# Write a Python program to find the common elements betweentwo lists.
# Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
# Sample output: [4, 5]

list1 = input("Write the elements for List 1: ")
list1 = list1.split()
list2 = input("Write the elements for List 2: ")
list2 = list2.split()
commonlist = list()

for i in list1:
    for j in list2:
        if i == j:
            commonlist.append(j)
 
print(commonlist)

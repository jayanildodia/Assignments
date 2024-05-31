# Write a Python program to create a list of given strings
# individually of the list using the Python map function.
# Eg. Input: ['Red', 'Blue', 'Black', 'White', 'Pink']
# Output: [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

def make_lists(x):
    newlist = list()
    for element in x:
        templist = list()
        for i in element:
            templist.append(i)
        print(f"Templist is {templist}")
        newlist.append(templist)
    print(f"List of elements in the list is: {newlist}")
    return newlist

x = input("Enter List of words using spaces: ").split()
make_lists(x)

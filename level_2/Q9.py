# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

def access_element_at_index(lst, index):
    try:
        element = lst[index]
        print(f"The element at index {index} is {element}.")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")

sample_list = input("Give a sample list with spaces inbetween: ")
sample_list = [int(a) for a in sample_list]
index = int(input("Enter an index to access: "))
access_element_at_index(sample_list, index)

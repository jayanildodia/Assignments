#Write a Python program to count the frequency of each elementin a list.
#Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
#Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
#training.consultadd.com

x = input("enter the list of numbers you want in the list with spaces inbetween: ")
listt = x.split()
dictionary = dict()
for element in listt:
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary[element] = 1
print(dictionary)

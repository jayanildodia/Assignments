# Write a Python program to reverse the order of words in a givensentence.
# Input_sentence = “Hello, World! Welcome to Pythonprogramming.”
# Output after reverse = “programming. Python to WelcomeWorld! Hello,”

x = input("Give a string as an input: ")
x = x.split()
lengthx = len(x)
newlist = list()
for i in range(1,lengthx+1):
    newlist.append(x[-i])
newlist = ' '.join(newlist)
print(newlist[:])

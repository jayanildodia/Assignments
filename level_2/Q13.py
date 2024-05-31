# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H"
# Sample Output: True

inp_str = input("Type the string: ")
y = input("Type a character: ")
x = lambda a: a in inp_str
print(x(y))

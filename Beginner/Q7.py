# Write a Python program to check if a string is an anagram ofanother string.
# string1 = "listen", string2 = "silent"
# Output: True

str1 = input("Type the first string: ")
str2 = input("Type the second string: ")
list_str1 = list(str1)
list_str2 = list(str2)

list_str1 = list_str1.sort()
list_str2 = list_str2.sort()

if list_str1 == list_str2:
    print("True")

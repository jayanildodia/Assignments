# Write a Python function that counts the number of vowels in a given string.
# Sample Input: string = "Hello, World!"
# Sample Output: Number of vowels: 3

def vowels(y):
    countvows = 0
    for i in y:
        if i in vows:
            countvows += 1
        else:
            continue
    return countvows

x = input("Write the string here: ")
y = x.lower()
y = [n for n in y]

vows = ['a', 'e', 'i', 'o', 'u']
total = vowels(y)
print(f"Total vowels in the given string '{x}' are {total}")

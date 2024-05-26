# Write a Python program to reverse a number using a whileloop.
# Sample Input: num = 12345
# Sample Output: revnum = 54321

x = list(input("give a number as an input: "))
start = 0
end = len(x) - 1

while start < end:
    x[start], x[end] = x[end], x[start]
    start += 1
    end -= 1

revx = ''.join(x)
print("Reversed string: ", revx)

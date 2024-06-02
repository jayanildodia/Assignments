# Given an input string, write a function that returns the run
# length encoded string for the input string.
# For Example:
# Input: wwwwaaadebbbbbw
# Output: w4a3d1e1b5w1

def encoded_string(input_str):
    result = ""
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i-1]:
            count += 1
        else:
            result += input_str[i-1] + str(count)
            count = 1
    result += input_str[-1] + str(count)
    return result

input_str = input("Enter a string full of repeated alphabets: ")
encoded_str = encoded_string(input_str)
print(encoded_str)

# Write a program to count the lines in a file “demo.txt”

def count_lines_in_file(filename):
    try:
        file = open(filename, 'r')
        try:
            lines = file.readlines()
            num_lines = len(lines)
        finally:
            file.close()
        return num_lines
    except FileNotFoundError:
        return "The file was not found."

filename = 'demo.txt'
line_count = count_lines_in_file(filename)
print(f"The number of lines in {filename} is: {line_count}")

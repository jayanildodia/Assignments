# Read the doc.txt file using Python File handling concept and return only the even length string from the file.
# Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string which is of even length.
# Make sure you return the content in The same link as it is present.

def get_even_length_strings(filename):
    try:
        file = open(filename, 'r')
        try:
            lines = file.readlines()
        finally:
            file.close()
            
        even_length_lines = []
        for line in lines:
            words = line.split()
            even_length_words = [word for word in words if len(word) % 2 == 0]
            even_length_lines.append(" ".join(even_length_words))
        return even_length_lines

    except FileNotFoundError:
        return "The file was not found."

filename = 'doc.txt'
even_length_content = get_even_length_strings(filename)
for line in even_length_content:
    print(line)

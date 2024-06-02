# Aditi has used text editing software to type some text. After
# saving the article as words.txt, she realized that she had wrongly
# typed the alphabet “J" instead of “I" everywhere in the article.
# Write a function definition for JtoI() in Python that would display
# the corrected version of the entire content of the file WORDS.TXT
# with all the alphabet "J" to be displayed as an alphabet "I" on the screen.
# Note: Assume that words.txt does not contain any J alphabet otherwise.

def JtoI(filename):
    try:
        file = open(filename, 'r')
        try:
            content = file.read()
            print("Original content in file is: {content}"")
        finally:
            file.close()

        corrected_content = ""
        for char in content:
            if char == 'J':
                corrected_content += 'I'
            else:
                corrected_content += char
        print("Corrected content in file is: {corrected_content}")

    except FileNotFoundError:
        print("The file was not found.")

filename = 'words.txt'
JtoI(filename)

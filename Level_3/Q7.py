# Write a program to construct a dictionary from the two lists containing the names
# of students and their corresponding subjects. The dictionary should map the students with
# their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
# Input: [Sam, Alice, Mona] ,[Commerce, Science, Computer]
# Output: [Sam: Commerce, Alice: Science , Mona: Computer]

students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

student_subjects = {}
for i in range(len(students)):
    student_subjects[students[i]] = subjects[i]

print("Using for loop:", student_subjects)

student_subjects_comprehension = {students[i]: subjects[i] for i in range(len(students))}
print("Using dictionary comprehension:", student_subjects_comprehension)

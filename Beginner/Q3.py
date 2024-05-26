# Write a Python program to input marks for five subjects Physics,Chemistry, Biology, Mathematics, and Computer.
# Calculate thepercentage and grade according to the following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

phy_marks = input("Input Marks for Physics out of 100: ")
chem_marks = input("Input Marks for Chem out of 100: ")
bio_marks = input("Input Marks for Biology out of 100: ")
math_marks = input("Input Marks for Mathematics out of 100: ")
comp_marks = input("Input Marks for Computers out of 100: ")

total_marks = int(phy_marks) + int(chem_marks) + int(bio_marks) + int(math_marks) + int(comp_marks)
percent = (total_marks/500)*100

if percent>=90:
    print("Grade A")
elif percent>=80:
    print("Grade B")
elif percent>=70:
    print("Grade C")
elif percent>=60:
    print("Grade D")
elif percent>=40:
    print("Grade E")
else:
    print("Grade F")

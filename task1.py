# Task 1: Create a Dictionary of Student Marks

Student_Marks = {
    "Rushi": 56, "Yogesh" : 68,
    "Prem" : 72, "Deepak" : 70,
    "Vishal" : 74
}
name = input("Enter the Student's name: ")
if name in Student_Marks.keys():
    print(f"{name}'s Marks: {Student_Marks[name]}")
else:
    print(f"{name} doesn't Found")


"""
Question: Student Grade Manager

Create a Python program that manages student grades using a dictionary.

Requirements:
1. Display the following menu repeatedly until the user chooses to exit.

===== Student Grade Manager =====
1. Add Student
2. View All Students
3. Find Average Grade
4. Find Highest Grade
5. Exit

2. Store student names as keys and their grades as values in a dictionary.

3. Menu Functions:
   - Add Student:
     • Ask for the student's name.
     • Ask for their grade (0–100).
     • If the student already exists, update their grade.

   - View All Students:
     • Display every student's name and grade.
     • If no students exist, display "No students found."

   - Find Average Grade:
     • Calculate and display the average grade with 2 decimal places.
     • If there are no students, display an appropriate message.

   - Find Highest Grade:
     • Display the name and grade of the student with the highest score.
     • If there are no students, display an appropriate message.

   - Exit:
     • Print "Goodbye!" and terminate the program.

Rules:
- Use a while loop for the menu.
- Use match-case to handle menu choices.
- Create a separate function to calculate the average grade.
- Validate that grades are between 0 and 100.
"""

students={}

def add_student():
    names=input("Enter student name: ").capitalize()
    try:
        grades=int((input("Enter student grade (0-100): ")))
    except ValueError:
        print("Please enter a numeric value.")
        return
    if 0<=grades<=100:
        students[names]=grades
    else:
        print("Please enter a grade between 0 and 100")

def view_all_students():
    if students:
        for name,grade in students.items():
            print(f"Student {name} has a grade: {grade}")
    else:
        print("No student found")

def average_grade():
    if students:
        avg=sum(students.values())/len(students)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No student found")

def highest_grade():
    if students:
        highest = max(students.values())
        for name,grade in students.items():
            if grade==highest:
                print(f"{name} has a highest grade: {highest}")
    else:
        print("No student found")

while True:
    print("\n----------------MENU-----------------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Find Average Grade")
    print("4. Find Highest Grade")
    print("5. Exit")
    print("---------------------------------------")
    print()
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue
    match choice:
        case 1:
            add_student()
        case 2:
            view_all_students()
        case 3:
            average_grade()
        case 4:
            highest_grade()
        case 5:
            print("Goodbye!")
            break
        case _:
            print("Please enter a valid choice")









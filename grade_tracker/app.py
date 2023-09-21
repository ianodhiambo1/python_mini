student_grades={}

def add_student(student_name):
    student_grades[student_name]={}

def add_grade(student_name,subject,grade):
    if student_name in student_grades:
        student_grades[student_name][subject]=grade
        print(f"Grade {grade} added for {student_name} in {subject}")
    else:
        print(f"Student {student_name} not found.")

def calculate_average(student_name):
    if student_name in student_grades:
        grades= student_grades[student_name].values() 
        average_grade = sum(grades) / len(grades)
        print(f"Average grade for {student_name}: {average_grade:.2f}")
    else:
        print(f"Student {student_name} not found.")


def display_student_information():
    print("Student Information:")
    for student_name, grades in student_grades.items():
        print(f"{student_name}: {grades}")

while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Calculate Average Grade")
    print("4. Display Student Information")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_name = input("Enter the student name: ")
        add_student(student_name)
    elif choice == '2':
        student_name = input("Enter the student name: ")
        subject = input("Enter the subject: ")
        grade = float(input("Enter the grade: "))
        add_grade(student_name, subject, grade)
    elif choice == '3':
        student_name = input("Enter the student name: ")
        calculate_average(student_name)
    elif choice == '4':
        display_student_information()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

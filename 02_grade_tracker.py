students = {}

def add_student(name):
    if name in students:
        print(f"{name} already exists")
    else:
        students[name] = []
        print(f"{name} added successfully")

def add_grade(name, grade):
    if name not in students:
        print(f"{name} not found")
    else:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}")

def calculate_average(name):
    if name not in students:
        print(f"{name} not found")
    elif len(students[name]) == 0:
        print(f"{name} has no grades yet")
    else:
        average = sum(students[name]) / len(students[name])
        print(f"{name}'s average is {average:.2f}")

def show_all_students():
    if len(students) == 0:
        print("No students yet")
    else:
        for name, grades in students.items():
            print(f"{name}: {grades}")

while True:
    print("\n--- Grade Tracker ---")
    print("1. Add student")
    print("2. Add grade")
    print("3. Calculate average")
    print("4. Show all students")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        add_student(name)
    elif choice == "2":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_grade(name, grade)
    elif choice == "3":
        name = input("Enter student name: ")
        calculate_average(name)
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
students = {}

def add_student(name):
    if name in students:
        print(f"{name} already exists.")
    else:
        students[name] = []
        print(f"{name} added successfully.")

def add_grade(name, grade):
    if name not in students:
        print(f"{name} does not exist.")
    else:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")

def calculate_average(name):
    if name not in students:
        print(f"{name} does not exist.")
    elif not students[name]:
        print(f"No grades for {name}.")
    else:
        average = sum(students[name]) / len(students[name])
        print(f"Average grade for {name}: {average:.2f}")


def show_all_students():
    if len(students) == 0:
        print("No students added.")
    else:
        for name, grades in students.items():
            print(f"{name}: Grades: {grades}")    


def main():
    while True:    
        print("\nGrade Tracker Menu:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Average")
        print("4. Show All Students")
        print("5. Exit")

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
            print("Exiting Grade Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
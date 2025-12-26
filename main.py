import json
import os


def load_students(filename="students.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


def save_students(students, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


def add_student(students):
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        student_id = students[-1]["id"] + 1 if students else 1

        students.append({
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        })

        save_students(students)
        print("Student added successfully!")
    except ValueError:
        print("Invalid input. Age must be a number.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")


def update_student(students):
    view_students(students)
    if not students:
        return

    try:
        student_id = int(input("Enter student ID to update: "))
        for student in students:
            if student["id"] == student_id:
                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["course"] = input("Enter new course: ")
                save_students(students)
                print("Student record updated!")
                return
        print("Student ID not found.")
    except ValueError:
        print("Invalid input.")


def delete_student(students):
    view_students(students)
    if not students:
        return

    try:
        student_id = int(input("Enter student ID to delete: "))
        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                save_students(students)
                print("Student record deleted!")
                return
        print("Student ID not found.")
    except ValueError:
        print("Invalid input.")


def student_management_app():
    students = load_students()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


student_management_app()

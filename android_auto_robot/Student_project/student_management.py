import json
import os


class StudentManagement:

    def __init__(self, file="students.json"):
        self.file = file
        self.students = self.load_data()

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return []

    # ---------------- SAVE DATA ----------------
    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.students, f, indent=4)

    # ---------------- ADD STUDENT ----------------
    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        student = {"id": sid, "name": name, "marks": marks}

        self.students.append(student)
        self.save_data()
        print("✅ Student Added Successfully")

    # ---------------- SEARCH STUDENT ----------------
    def search_student(self):
        sid = input("Enter Student ID to Search: ")

        for student in self.students:
            if student["id"] == sid:
                print(student)
                return

        print("❌ Student Not Found")

    # ---------------- UPDATE MARKS ----------------
    def update_marks(self):
        sid = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == sid:
                new_marks = int(input("Enter New Marks: "))
                student["marks"] = new_marks
                self.save_data()
                print("✅ Marks Updated")
                return

        print("❌ Student Not Found")

    # ---------------- DELETE STUDENT ----------------
    def delete_student(self):
        sid = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student["id"] == sid:
                self.students.remove(student)
                self.save_data()
                print("✅ Record Deleted")
                return

        print("❌ Student Not Found")


# ---------------- MENU ----------------
def menu():
    system = StudentManagement()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.search_student()
        elif choice == "3":
            system.update_marks()
        elif choice == "4":
            system.delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")


menu()

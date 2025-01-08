import sys


class Student:
    def __init__(self, i=None, n=None, b=None):
        self.i = i
        self.n = n
        self.b = b

    def input(self):
        self.i = input("Student id: ")
        self.n = input("Student name: ")
        self.b = input("Student DoB: ")

    def __str__(self):
        return f"""Student id: {self.i}\nStudent name: {self.n}\nStudent DoB: {self.b}"""


class Course:
    def __init__(self, i=None, n=None):
        self.i = i
        self.n = n
        self.m = {}  # Marks dictionary for students

    def input(self):
        self.i = input("Course id: ")
        self.n = input("Course name: ")

    def __str__(self):
        res = f"""Course id: {self.i}\nCourse name: {self.n}\nCourse marks:"""
        for stid, mark in self.m.items():
            res += f"\n\tStudent ID {stid}: {mark}"
        return res


def student_input(std_list):
    print("----------------------")
    nb = int(input("Number of students: "))
    for idx in range(nb):
        print(f"Student number {idx + 1}:")
        st = Student()
        st.input()
        print("----------------------")
        std_list.append(st)


def courses_input(cs_list):
    print("----------------------")
    nb = int(input("Number of courses: "))
    for idx in range(nb):
        print(f"Course number {idx + 1}:")
        cs = Course()
        cs.input()
        print("----------------------")
        cs_list.append(cs)


def mark_input(cs_list, std_list):
    print("----------------------")
    csid = input("Select the course by Course ID: ")
    cs = next((cs for cs in cs_list if cs[0] == csid), None)
    # cs = [cs for cs in cs_list if cs[0] == csid][0]
    if not cs:
        print("Course not found.")
        return

    print("Please insert student marks:")
    for st in std_list:
        print("+++")
        mrk = input(f"Student {st.n} [{st.i}] mark: ")
        cs.m[st.i] = mrk
    print("----------------------")


def student_list(std_list):
    print("----------------------")
    print(f"There are {len(std_list)} students in the system:")
    for st in std_list:
        print("+++")
        print(st)
    print("----------------------")


def courses_list(cs_list):
    print("----------------------")
    print(f"There are {len(cs_list)} courses in the system:")
    for cs in cs_list:
        print("+++")
        print(cs)
    print("----------------------")


def mark_list(cs_list):
    print("----------------------")
    print("Marks information for all courses:")
    for cs in cs_list:
        print("+++")
        print(cs)
    print("----------------------")


if __name__ == "__main__":
    std_list = []
    cs_list = []

    # input = sys.stdin.read if not sys.stdin.isatty() else input
    
    while True:
        option = int(
            input(
                """
[Student Mark Management System]
1. Insert students
2. Insert courses
3. List student info
4. List course info
5. Add marks
6. Display marks
7. Exit
Option: """
            )
        )

        if option == 1:
            student_input(std_list)
        elif option == 2:
            courses_input(cs_list)
        elif option == 3:
            student_list(std_list)
        elif option == 4:
            courses_list(cs_list)
        elif option == 5:
            mark_input(cs_list, std_list)
        elif option == 6:
            mark_list(cs_list)
        elif option == 7:
            break
        else:
            print("Invalid option.")

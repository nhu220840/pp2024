# Student = [id, name, DoB]
# Course [id, name, {stid: stmark}]

# stlst = [Student, etc.]
# cslst = [Course, etx.]

import math
import sys
import numpy as np

class Student:
    def __init__(self, i=None, n=None, b=None):
        self.i = i
        self.n = n
        self.b = b
        self.gpa = 0

    def input(self):
        self.i = input("Student id: ")
        self.n = input("Student name: ")
        self.b = input("Student DoB: ")

    def __str__(self):
        return f"""Student id: {self.i}\nStudent name: {self.n}\nStudent DoB: {self.b}\nStudent GPA: {self.gpa}"""


class Course:
    def __init__(self, i=None, n=None, credits=None):
        self.i = i
        self.n = n
        self.credits = credits
        self.m = {}  # Marks dictionary for students

    def input(self):
        self.i = input("Course id: ")
        self.n = input("Course name: ")
        self.credits = int(input("Course credits: "))

    def __str__(self):
        res = f"""Course id: {self.i}\nCourse name: {self.n}\nCourse credits: {self.credits}\nCourse marks:"""
        for stid, mark in self.m.items():
            res += f"\n\tStudent ID {stid}: {mark}"
        return res

###################### STUDENT MANAGEMENT SYSTEM ######################

def student_input(std_list):
    print("----------------------")
    nb = int(input("Number of students: "))
    for idx in range(nb):
        print(f"Student number {idx + 1}:")
        st = Student()
        st.input()
        print("----------------------")
        std_list.append(st)

def student_list(std_list):
    print("----------------------")
    print(f"There are {len(std_list)} students in the system:")
    for st in std_list:
        print("+++")
        print(st)
    print("----------------------")

###################### STUDENT MANAGEMENT SYSTEM ######################

###################### COURSES MANAGEMENT SYSTEM ######################

def courses_input(cs_list):
    print("----------------------")
    nb = int(input("Number of courses: "))
    for idx in range(nb):
        print(f"Course number {idx + 1}:")
        cs = Course()
        cs.input()
        print("----------------------")
        cs_list.append(cs)

def courses_list(cs_list):
    print("----------------------")
    print(f"There are {len(cs_list)} courses in the system:")
    for cs in cs_list:
        print("+++")
        print(cs)
    print("----------------------")

###################### COURSES MANAGEMENT SYSTEM ######################

####################### MARK MANAGEMENT SYSTEM #######################

def mark_input(cs_list, std_list):
    print("----------------------")
    csid = input("Select the course by Course ID: ")
    cs = next((cs for cs in cs_list if cs.i == csid), None)
    if not cs:
        print("Course not found.")
        return

    print("Please insert student marks:")
    for st in std_list:
        print("+++")
        mark = float(input(f"Student {st.n} [{st.i}] mark: "))
        cs.m[st.i] = mark
    print("----------------------")

def mark_list(cs_list):
    print("----------------------")
    print("Marks information for all courses:")
    for cs in cs_list:
        print("+++")
        print(cs)
    print("----------------------")

def calculate_gpa(cs_list, std_list):
    print("----------------------")
    print("Calculating GPA for all students:")
    for st in std_list:
        print("+++")
        weighted_marks = [
            cs.m[st.i] * cs.credits
            for cs in cs_list
            if st.i in cs.m
        ]
        total_credits = sum(cs.credits for cs in cs_list if st.i in cs.m)
        st.gpa = sum(weighted_marks) / total_credits if total_credits > 0 else 0
        # Round to 1 decimal place
        rounded_gpa = round(st.gpa, 1)
        print(f"Student {st.n} [{st.i}] has GPA: {rounded_gpa}")
    print("----------------------")

def sort_by_gpa(std_list):
    return sorted(std_list, key=lambda x: x.gpa, reverse=True)

####################### MARK MANAGEMENT SYSTEM #######################

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
7. Calculate GPA
8. Sort by GPA
9. Exit
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
            calculate_gpa(cs_list, std_list)
        elif option == 8:
            sorted_list = sort_by_gpa(std_list)
            print("----------------------")
            print("Students sorted by GPA:")
            for st in sorted_list:
                print("+++")
                print(st)
            print("----------------------")
        elif option == 9:
            break
        else:
            print("Invalid option.")

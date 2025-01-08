# Student = [id, name, DoB]
# Course [id, name, {stid: stmark}]

# stlst = [Student, etc.]
# cslst = [Course, etx.]

def std_inpf(stlst):
    print("----------------------")
    nb = int(input("Number students: "))
    for idx in range(nb):
        print(f"Student number: {idx + 1}")
        i = input("Student id: ") 
        n = input("Student name: ")
        b = input("Student DoB: ")       
        print("----------------------")
        stlst.append([i, n, b])

def cs_inpf(cslst):
    print("----------------------")
    nb = int(input("Number courses: "))
    for idx in range(nb):
        print(f"Courses number: {idx + 1}")
        i = input("Course id: ") 
        n = input("Course name: ")
        print("----------------------")
        cslst.append([i, n, {}])

def mrk_inpf(cslst, stlst):
    print("----------------------")
    csid = input("Select the couse by courst ID: ")
    cs = next((cs for cs in cslst if cs[0] == csid), None)
    if not cs:
        print("Course not found.")
        return
    
    print("Please insert student marks: ")
    for st in stlst:
        print("+++")
        mrk = input(f"Student {st[1]}[{st[0]}] mark: ")
        cs[2][st[0]] = mrk
    print("----------------------")

def std_lstf(stlst):
    print("----------------------")
    print(f"There are {len(stlst)} in system: ")
    for st in stlst:
        print("+++")
        print(f"Student id: {st[0]}")
        print(f"Student name: {st[1]}")
        print(f"Student DoB: {st[2]}")
    print("----------------------")

def cs_lstf(cslst):
    print("----------------------")
    print(f"There are {len(cslst)} in system: ")
    for cs in cslst:
        print("+++")
        print(f"Course id: {cs[1]}")
        print(f"Course name: {cs[0]}")
        print(f"Course mark: ")
        for k, v in cs[2].items():
            print(f"\t Student [{k}] has mark: {v}") 
    print("----------------------")

if __name__ == "__main__":
    stlst = []
    cslst = []
    while True:
        opt = int(
            input(
            """
[Student mark managament]
1. Insert students
2. Insert courses
3. List student info
4. List course info
5. Add mark
6. List mark
7. Exit
Opt:
""" 
                )
            )

        if opt == 1:
            std_inpf(stlst)
        elif opt == 2:
            cs_inpf(cslst)
        elif opt == 3:
            std_lstf(stlst)
        elif opt == 4:
            cs_lstf(cslst)
        elif opt == 5:
            mrk_inpf(cslst, stlst)
        elif opt == 6:
            cs_lstf(cslst)
        elif opt == 7:
            break
        else:
            print("Option does not exist")()


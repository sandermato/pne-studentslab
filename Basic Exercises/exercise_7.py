
def enrolled(student):
    flag = False
    for i in range(0,len(student["subjects"])):
        if student["subjects"][i] == "PNE":
            flag = True
    return flag

def average_grade(student):
    alls = 0
    sums = 0
    for key, value in student["grades"].items():
        sums += value
        alls += 1
    average = sums/alls
    return average

def grade_show(student):
    print("Subject grades:")
    for key, value in student["grades"].items():
        print("  ",key,":",value)

if __name__ == "__main__":
    student = {
        "name": "Carlos",
        "age": 22,
        "subjects": ["PNE", "Networks", "Databases"],
        "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
    }
    print("Name:", student['name'])
    print("Number of subjects:", len(student['subjects']))
    print("Enrolled in PNE:", enrolled(student))
    print("Databases grade:", student["grades"]["Databases"])
    print("Average grade:", round(average_grade(student),2))
    grade_show(student)

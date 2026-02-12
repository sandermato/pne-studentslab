
def average(grades):
    for i in range(0, len(grades)):
        sums = 0
        length = 0
        for a in grades[i]['grades']:
            sums += a
            length += 1
        average = sums/length
        grades[i]["average"] = round(average,1)
    return grades

def get_status(avg):
    for i in range(0, len(avg)):
        pass_grade = "FAIL"
        if avg[i]["average"] > 5.0:
            pass_grade = "PASS"
        print(avg[i]["name"],":", avg[i]["average"],"->", pass_grade )

if __name__ == "__main__":
    students = [
        {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
        {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
        {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
        {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
        {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
    ]
    students = average(students)
    get_status(students)


def scored(grade):
    if 9.0 <= grade <= 10.0:
        output = "A"
    elif 7.0 <= grade < 9.0:
        output = "B"
    elif 5.0 <= grade < 7.0:
        output = "C"
    elif 3.0 <= grade < 5.0:
        output = "D"
    elif 0.0 <= grade < 3.0:
        output = "F"
    return output



if __name__ == "__main__":
    #grade = input("Enter exam grade:")
    grade1 = 9.5
    grade2 = 7.0
    grade3 = 5.5
    grade4 = 3.2
    grade5 = 1.0
    print("Score", grade1, "->", scored(grade1))
    print("Score", grade2, "->", scored(grade2))
    print("Score", grade3, "->", scored(grade3))
    print("Score", grade4, "->", scored(grade4))
    print("Score", grade5, "->", scored(grade5))
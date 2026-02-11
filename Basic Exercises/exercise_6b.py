
def classify_triangle(a, b, c):
    if a==b and a==c and b==c:
        triangle = "equilateral"
    elif a==b or a==c or b==c:
        triangle = "isosceles"
    else:
        triangle = "scalene"
    return triangle

if __name__ == "__main__":
    print("classify_triangle(5, 5, 5) =", classify_triangle(5, 5, 5))
    print("classify_triangle(3, 3, 4) =", classify_triangle(3, 3, 4))
    print("classify_triangle(3, 4, 5) =", classify_triangle(3, 4, 5))
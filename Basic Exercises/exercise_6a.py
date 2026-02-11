
def is_even(number):
    if number % 2 == 0:
        even = "True"
    else:
        even = "False"
    return even

if __name__ == "__main__":
    list = [4, 7, 0, -3, 10]
    for i in range(0,len(list)):
        print("is_even(",list[i],") =", is_even(list[i]))
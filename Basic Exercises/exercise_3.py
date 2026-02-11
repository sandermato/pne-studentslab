
def max(temp):
    max = 0
    i = 0
    while i < len(temp):
        if temp[i] > max:
            max = temp[i]
        i += 1
    return max

def min(temp):
    min = 1000
    i = 0
    while i < len(temp):
        if temp[i] < min:
            min = temp[i]
        i += 1
    return min

def average(temp):
    total = 0
    for i in range(0, len(temp)):
        total += temp[i]
    total = total/len(temp)
    return total

def above(temp):
    limit_pass = 0
    for i in range(0, len(temp)):
        if temp[i] > 18:
            limit_pass += 1
    return limit_pass

def sorted(temp):
    list = []
    length = len(temp)
    while len(list) < length:
        min = 1000
        i = 0
        while i < len(temp):
            if temp[i] < min:
                min = temp[i]
            i += 1
        temp.remove(min)
        list.append(min)
    return list

if __name__ == "__main__":
    temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
    print("Wednesday:", temperatures[2])
    print("Max:", max(temperatures))
    print("Min:", min(temperatures))
    print("Average:", round(average(temperatures), 1))
    print("Days above 17:", above(temperatures))
    print("Sorted:", sorted(temperatures))
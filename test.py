print("Please input 10 numbers")
print("input first number")
n1 = int (input(">"))
print("please input second number")
n2 = int (input(">"))
print("please input third number")
n3 = int (input(">"))
print("please input fourth number")
n4= int (input(">"))
print("please input fifth number")
n5 =int (input(">"))
print("please input sixth number")
n6 = int (input(">"))
print("please input seventh number")
n7 = int (input(">"))
print("please input eigth number")
n8 =int (input(">"))
print("please input ninth number")
n9 = int (input(">"))
print("please input tenth number")
n10 =int (input(">"))
numbers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
def calculate_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum/ten (numbers)



avg = calculate_average(numbers)

print(f"Your average is: {avg}")

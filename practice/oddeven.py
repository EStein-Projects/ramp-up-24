def even_tester(n):
    if not type(n) == int:
        print("Invalid Input")
    elif n%2 == 0:
        print("Integer is even")
    else:
        print("Integer is odd")

num = input("Enter an integer: ")
try:
    num = int(num)
    even_tester(num)
except ValueError:
    print("Invalid Input")
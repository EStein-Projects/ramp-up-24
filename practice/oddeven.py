def even_tester(n):
    integer = 0
    try:
        integer = int(n)
        if isinstance(n, float):
            print("Invalid input. Please enter a valid integer.")
        elif integer%2 == 0:
            print("Integer is even.")
        else:
            print("Integer is odd.")
    except (ValueError or TypeError):
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    even_tester(input("Enter an integer: "))
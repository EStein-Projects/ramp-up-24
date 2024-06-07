def even_tester(n):
    if isinstance(n, float):
            print("Invalid input. Please enter a valid integer.")
    n = int(n)
    if n%2 == 0:
        return True
    return False

if __name__ == '__main__':
    n = int(input("Enter an integer: "))
    even = even_tester(n)
    if even:
        print("Integer is even.")
def str_reverser(s):
    if not isinstance(s, str):
        print("Invalid input. Please enter a valid string.")
    else:
        r = ""
        v_count = 0
        vowels = "aeiou"
        for c in reversed(s):
            r += c
            if c in vowels:
                v_count += 1
        print(f"The string reversed is \"{r}\" and the number of vowels in it is {v_count}.")

if __name__ == '__main__':
    str_reverser(input("Enter a string: "))
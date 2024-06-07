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
        return [r, v_count]
        

if __name__ == '__main__':
    data = str_reverser(input("Enter a string: "))
    print(f"The string reversed is \"{data[0]}\" and the number of vowels it contained is {data[1]}.")
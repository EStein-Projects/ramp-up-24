def int_stats (nums):        
    try:
        if isinstance (nums, str):
            nums = [n for n in nums.split()]
        x = int(nums[0])
        min = x
        max = x
        sum = 0
        for n in nums:
            x = int(n)
            if x < min:
                min = x
            if x > max:
                max = x
            sum += x
        print (f"The sum of this list of integers is {sum},\nthe smallest integer in the list is {min},\nthe biggest one is {max},\nand the average value of the list is {sum/len(nums)}")
    except (ValueError, TypeError):
        print("Invalid input. Please enter a valid list of integers.")

if __name__ == '__main__':
    int_stats(input("Enter a list of integers without brackets and separated by a space: "))

 # type: ignore
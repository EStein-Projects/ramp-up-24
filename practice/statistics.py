def int_stats (nums):
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
    return [sum, min, max, sum/len(nums)]

if __name__ == '__main__':
    nums = (input("Enter a list of integers without brackets and separated by a space: "))
    nums = [n for n in nums.split()]
    stats = int_stats(nums)
    print (f"The sum of this list of integers is {stats[0]},\nthe smallest integer in the list is {stats[1]},\nthe biggest one is {stats[2]},\nand the average value of the list is {stats[3]}.")

 # type: ignore
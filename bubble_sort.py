# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# a) Bubble Sort


def bubblesort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums = [3,6,1,9,2,5,7]
bubblesort(nums)
print(nums)

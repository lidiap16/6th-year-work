def insertionSort(nums):
    n = len(nums)
    
    for i in range(1, n):  # Iterate through all the nums
        key = nums[i]  #key is the num being compared
        j = i-1
        while j >= 0 and key < nums[j]: 
            nums[j+1] = nums[j]  # Shift elements to the right
            j -= 1  #-1 it compares with the number to the left 
        nums[j+1] = key  # Insert key in the correct position
 
nums = [10, 9,2, 5, 6]
insertionSort(nums)
print(nums)
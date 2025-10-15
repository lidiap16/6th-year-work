nums = [27, 13, 32, 50, 16,22]

 # Display the list
print("The initial list of values is:", nums)

 # Sort the list
nums.sort()

 # Display the sorted list
print("The sorted list of values is:", nums)
 # Determine the median
N = len(nums)
if N == 0:
    print("The list is empty. Cannot compute the median.")
else:
    if N % 2 != 0:
        median = nums[N//2]
    else:
        median = (nums[N//2-1] + nums[N//2])/2

#Display the median
print("The median is", median)
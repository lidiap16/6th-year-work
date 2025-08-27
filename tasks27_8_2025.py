#Task 1  

# print(12+7) 
# 
# print(15//4) 
# 
# print(5**3) 
# 
#   
# 
# #Task 2  
# 
# #String 
# 
# #Float 
# 
# #Boolean 
# 
# #Integer 
# 
# 
# #Task3 
# 
# #You are too young 
# 
# age = 17 
# 
# if age>=18: 
# 
# 	print("you can vote") 
# 
# elif age==17: 
# 
# 	print("almost there") 
# 
# else: 
# 
# 	print("you are too young") 
# 
#  
# 
# # #task 4 
# 
# for i in range(0,10): 
# 
# 	print(i+1) 
# 
# input=1 
# 
# while input!=0: 
# 
#     input=int(input("enter a number"))

 
# 
# #task 5 
# 
# nums = [4,7,2,9,6,] 
# 
# print(nums[0]) 
# 
# print(nums[-1])
# 
# nums.append(12) 
# 
# nums.sort()
# 
# print(nums)

# #task6 
# 
# def square(x): 
# 
# 	 
# 
# 	x=x*x 
# 
# 	print("new num =", x) 
# 
# 	return 
# 
# x=int(input("enter num"))
# 
# square(x) 
# 
# 	 

# def is_even(n): 
# 
# 	if n%2==0: 
# 
# 		return True 
# 
# 	else: 
# 
# 		return False 
# 
# n= int(input("enter num")) 
# 
# is_even(n) 
# print(is_even(n))
 

# #task7  
#not working
# counter = 0 
# mean = 0
# mode = 0
# data = [5,3,8,3,9,12,5,3] 
# 
# for i in range(0,len(data)):
#     mean =mean +data[i]
#     counter=data.count[i] 
# 
# if counter >0: 
#     i = mode 
# 
# print("the mean", mean) 
# 
# print("the mode", mode) 

 

 
# 
# #task8 

# list = [] 
# 
# for i in range(0,5): 
# 
# 	user=int(input("enter num"))
# 
# 	list.append(user) 
# 
# for i in range(0,5):
#     if list[i]%2==0:
#         print(list[i]) 

 

# #task 9 
# 
# def get_range(range): 
# 
# 	values.sort() 
# 
# 	range = (values[-1]-values[0]) 
# 
# 	print("the range is" , range) 
# 
# values= []
#
def get_range(values): 

    return max(values) - min(values) 

nums = [4,7,1,9,3]
print("range", get_range(nums))





import statistics 

 

def get_range(values): 

    return max(values) - min(values) 

 


numbers = [] 

for i in range(6): 

    num = float(input("Enter number: ")) 

    numbers.append(num) 

 

# Calculate values 

mean = statistics.mean(numbers) 

median = statistics.median(numbers) 

mode = statistics.mode(numbers) 

maximum = max(numbers) 

minimum = min(numbers) 

range_val = get_range(numbers) 


print("Data Analysis Results") 

print("Numbers:", numbers) 

print("Mean:", mean) 

print("Median:", median) 

print("Mode:", mode) 

print("Maximum:", maximum) 

print("Minimum:", minimum) 

print("Range:", range_val)  
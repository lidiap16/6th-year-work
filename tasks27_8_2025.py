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

# mean = 0
# mode = 0
# data = [5,3,8,3,9,12,5,3] 
# mean = sum(data) / len(data)
# count = data[0]
# most_count = 0
# for i in range(len(data)):
#     frequ = 0
#     for y in range(len(data)):
#         if data[y] == data[y]:
#             frequ += 1
#         if frequ > most_count:
#             most_count = frequ
#             mode = data[i]
# 
# data.sort()
# 
# print("the mean", mean) 
# 
# print("the mode", mode) 
# print("smallest", data[0])
# print("largest", data[-1])
#  

 

#task8 

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
# 
#  
# 
# #task 9 


##def get_range(nums): 
# 
#     return max(nums) - min(nums) 
# 
# nums = [4,7,1,9,3]
# print("range", get_range(nums))
# 
# 

# 
# task10

# 
def get_range(values): 

    return max(values) - min(values) 

def get_mean(values):
     return sum(values) / len(values)
    
def get_median(values):
    values = sorted(values)
    n = len(values)
    mid = n// 2
    if n % 2 == 0:
        return (values[mid-1] +values[mid]) / 2
    else:
        return values[mid]


#
def get_mode(values):
    count = values[0]
    most_count = 0     
    mode = 0
    for i in range(len(values)):
        frequ = 0
        for y in range(len(values)):
            if values[i] == values[y]:
                frequ += 1
                
        if frequ > most_count:
            most_count = frequ
            mode = values[i]
    return mode     


def get_max(values):
    return max(values)

def get_min(values):
    return min(values)

numbers = [] 
for i in range(6): 

    num = float(input("Enter number: ")) 

    numbers.append(num) 

 





range_val = get_range(numbers) 


print("Numbers:", numbers) 

print("Mean:", get_mean(numbers)) 

print("Median:", get_median(numbers)) 

print("Mode:", get_mode(numbers)) 

print("Maximum:", get_max(numbers)) 

print("Minimum:", get_min(numbers)) 

print("Range:", range_val)  

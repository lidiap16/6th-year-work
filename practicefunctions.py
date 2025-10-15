def shop_list(items):
    for item in items:
        print(item)
        
fruits = ["apples","banana","olives"]
shop_list(fruits)

def total(numbers):
    result = 0
    for n in numbers:
        result = result +n
    return result
scores = [10,20,30]
print(total(scores))

def ave(numbers):
    average = sum(numbers)/len(numbers)
    return average
    
nums = [1,2,3]
print(ave(nums))


def search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

numbers = [2,3,4,5,6,7]
print(search(numbers,5))
print(search(numbers,1))

def count(items, number):
    count = 0
    for item in items:
        if item == number:
            count += 1
    return count
letters = ["a","b","a","d"]
print(count(letters,"a"))

def short_list(words):
    newlist = []
    for word in words:
        if len(word) <= 4:
            newlist.append(word)
    return newlist
    
    
word_list = ["lol", "hello","happy","yolo"]
print(short_list(word_list))


names = ["sarah","tom","liam"]

# search ="tom"
# found = False
# 
# for name in names:
#     if name == search:
#         found = True
#         
# if found:
#     print("found")
# else:
#     print("not there ")
    
def find(names, target):
    for name in names:
        if name == target:
            return name
    return -1

names = ["sarah","tom","liam"]
print(find(names, "lid"))
        


#lidia

def binary_search(v, list):
    low = 0
    high = len(list)-1
    
    while (low <= high):#
        mid = (low+high)//2
        
        if list[mid] == v:
            return mid
        elif list[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1


keys = [3,17,21,39,57,63,71,100]
argument = int(input("enter a target value:"))

result = binary_search(argument, keys)

if (result != -1):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for i in range(ind + 1, size): 
            if array[i] < array[min_index]:
                min_index = i
        (array[ind], array[min_index]) = (array[min_index], array[ind])

nums = [-3, 5, 0, 10,7, 20,4]
size = len(nums)
selectionSort(nums, size)
print(nums)
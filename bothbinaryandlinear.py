import random
import matplotlib.pyplot as plt




def binary_search(v, L):
    comparisons = 0
    low, high = 0, len(L) - 1
    while low <= high:
        index = (low+high)//2
        comparisons = comparisons + 1
        if L[index] == v:
            return index, comparisons
        elif L[index] < v:
            low = index + 1
        else:
            high = index - 1
    return -1, comparisons



def linear_search(v, L):
    comparisons = 0
    for index in range(len(L)):
        comparisons = comparisons + 1
        if L[index] == v:
            return index, comparisons
    return -1, comparisons # not found


list_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256,
              512, 1024, 2048, 4096, 8192,
              16384, 32768, 65536]


results = []



for size in list_sizes:
    some_list = list(range(size))

    # ---- Binary Search ----
    # Case 1: Target exists (random)
    target = random.choice(some_list) if some_list else -1
    _, comp_exist_b = binary_search(target, some_list)

    # Case 2: Target does not exist (-1 never in list)
    _, comp_not_b = binary_search(-1, some_list)

    # ---- Linear Search ----
    random.shuffle(some_list)  # randomize order
    # Case 1: Target exists (random)
    target = random.choice(some_list) if some_list else -1
    _, comp_exist_l = linear_search(target, some_list)

    # Case 2: Target does not exist (-1 never in list)
    _, comp_not_l = linear_search(-1, some_list) # _, means ignore first value

    results.append([size, comp_not_b, comp_exist_b, comp_not_l, comp_exist_l])

print(f"{'List Size':>8} | {'Bin Not Exist':>12} | {'Bin Exist':>9} | {'Lin Not Exist':>13} | {'Lin Exist':>9}")
print("-" * 65)
for row in results:
    print(f"{row[0]:>8} | {row[1]:>12} | {row[2]:>9} | {row[3]:>13} | {row[4]:>9} |")
    
    
    
    
sizes = [r[0] for r in results]
bin_not = [r[1] for r in results]
bin_yes = [r[2] for r in results]
lin_not = [r[3] for r in results]
lin_yes = [r[4] for r in results]

plt.figure(figsize=(10,6))
plt.plot(sizes, bin_not, label="Binary Search (Not Exist)", marker="x")
plt.plot(sizes, bin_yes, label="Binary Search (Exists)", marker="o")
plt.plot(sizes, lin_not, label="Linear Search (Not Exist)", marker="x")
plt.plot(sizes, lin_yes, label="Linear Search (Exists)", marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("List Size (log scale)")
plt.ylabel("Comparisons (log scale)")
plt.title("Binary Search vs Linear Search Comparisons")
plt.legend()
plt.show()
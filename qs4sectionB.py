#lidia pasiecznik

items = []
prices = []

print("Shopping Trip Calculator")

item_num = int(input("how many items do you want to add:"))

for i in range(item_num):
    item = input("item name:")
    items.append(item)
    price = input(f"how much is {item}: ")
   # if price <0:
        
    prices.append(float(price))
    
def item_list():
    print("item shopping list and price")
    print("-" * 20)
    for i in range(item_num):
        print(f"{items[i]}   ${prices[i]}")
        
item_list()

total = round(sum(prices),2)
print(f"total is {total}")

most_expensive = max(prices)
itempossition = (prices.index(most_expensive))
print(f"{items[itempossition]} is the most expensive, at a price of ${most_expensive}")

least_expensive = min(prices)
itempossition2 = (prices.index(least_expensive))
print(f"{items[itempossition2]} is the least expensive, at a price of ${least_expensive}")
#
ave = sum(prices)/ len(items)
print(f"average is {round(ave,2)} ")



budget = float(input("what is your budget:"))
if total <= budget:
    print("you are within the budget")
    diff = budget - total
    print(f" you have ${diff} left")
else:
    print("you are over the budget")
    diff2 = total - budget
    print(f" you are ${diff2} over budget")
for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
        if prices[i] < prices[j]:
            prices[i], prices[j] = prices[j], prices[i]
            items[i], items[j] = items[j], items[i]
            
for i in range(len(items)):
    print(f"{items[i]}  ${prices[i]}")
    
 

# Enter name:

county = ["Dublin", "Laois", "Dublin", "Dublin", "Dublin", "Dublin", "Dublin", "Kildare", "Laois", "Kildare", "Dublin", "Laois", "Dublin"]

rent = [2500, 1200, 2000, 2100, 1900, 1999, 1790, 1500, 1000, 1390, 1980, 1105, 1999]

# Part i

print("The total people in the survey is:", len(county))
# Part ii
addCounty = input("Enter your count:")
county.append(addCounty)
addRent = int(input("Enter your rent:"))
rent.append(addRent)


print("-"*18)
print("{:<13}".format("County")+"{:<13}".format("Rent €"))
print("-"*18)
for index in range(len(county)):
    print("{:<13}".format(county[index])+"{:<13}".format(rent[index]))

# Part iii
totalave = 0
for i in range(len(rent)):
    totalave += rent[i]
 
average = totalave / 14
print(average)
#                
#totalave = sum(rent)  ~forgottt to make the input line into an integerrrrr line 14  whoopsssss 
               
               
#                
#                
# averent = sum(rent) / 3
# print("average rent for all counties:", averent)

# Part iv

tottalDub = 0
tottalKil = 0
tottalLao = 0

counter1 = 0
counter2 = 0
counter3 = 0
for i in range(len(county)):
    if county[i] == "Dublin":
        tottalDub += rent[i]
        counter1 += 1
    elif county[i] == "Kildare":
        tottalKil += rent[i]
        counter2 += 1
    else:
        tottalLao += rent[i]
        counter3 += 1

aveDub = tottalDub / counter1
aveKil = tottalKil / counter2
aveLao = tottalLao / counter3

print("average rent for dublin: €",aveDub)
print("average rent for Kildare: €",aveKil)
print("average rent for Laois: €",aveLao)        
        
        
# Question 16 (a)
# Examination Number:

def get_grade(result):
    grade = "Unsuccessful"

    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 55:
        grade = "lower Merit"
    elif result >= 40:
        grade = "pass"
    else:
        grade = "unsuccessful"

        
    


    return grade

 # Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0
lowest = min(results)
highest = max(results)
#Loop N times
for i in range(N):
    total = total + results[i] # Running total
count1 = 0
for result in results:
    if result <= 40:
        count1 +=1
        
count2 =0
for result in results:
    if result <= 79 and result >= 50:
        count2 +=1            
    

 # Divide by the total number of results to give the mean
arithmetic_mean = total/len(results)

 # Display the answer
print("The mean percentage mark is", round(arithmetic_mean, 2))
print("the grade for the average is", get_grade(arithmetic_mean))
print("lowest", lowest)
print("highest", highest)
print("the number of scores lower than 40 is ", count1)
print("the number of scores between 50 and 79 inclusive is", count2)


longest_run = []
current_run = [results[0]]

for i in range(1, N):
    if results[i] > results[i - 1]:
        current_run.append(results[i])
    else:
        if len(current_run) > len(longest_run):
            longest_run = current_run
            current_run = [results[i]]

 # Check one last time at the end of the loop
if len(current_run) > len(longest_run):
    longest_run = current_run

print("Longest run of result increases is", longest_run)
 # part (vii) - end


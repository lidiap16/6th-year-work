# Enter name: 

import random

targetWord = "THE"

def monkeys_typing():
    guessNumber1 = random.randint(65, 90)
    letter1 = chr(guessNumber1)
    count1 = 1
    guess1 = letter1
    
    guessNumber2 = random.randint(65, 90)
    letter2 = chr(guessNumber2)
    count2 = 1
    guess2 = letter2
    
    guessNumber3 = random.randint(65, 90)
    letter3 = chr(guessNumber3)
    count3 = 1
    guess3 = letter3
    print(guess1 + guess2 + guess3)
    word =(guess1 + guess2 + guess3)

    
    while word != targetWord:
        guessNumber1 = random.randint(65, 90)
        letter1 = chr(guessNumber1)
        guess1 = letter1
 #       print(guess1)
        count1 +=1
        guessNumber2 = random.randint(65, 90)
        letter2 = chr(guessNumber2)
        guess2 = letter2
 #       print(guess2)
        count2 +=1
        guessNumber3 = random.randint(65, 90)
        letter3 = chr(guessNumber3)
        guess3 = letter3
#        print(guess3)
        count3 +=1
        word =(guess1 + guess2 + guess3)
        print(word)
   # while
        
        
#         guess2 != targetWord[1]
#         guessNumber2 = random.randint(65, 90)
#         letter2 = chr(guessNumber2)
#         guess2 = letter2
#         print(guess2)
#         count2 +=1
#     
#     #while
#         guess3 != targetWord[2]
#         guessNumber3 = random.randint(65, 90)
#         letter3 = chr(guessNumber3)
#         guess3 = letter3
#         print(guess3)
#        count3 +=1
        
    return (count1 + count2 + count3)

#print(monkeys_typing())

total = monkeys_typing() + monkeys_typing() + monkeys_typing()
average = total / 3
print("Average number of guesses for three runs is:", average)

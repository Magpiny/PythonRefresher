# LOOPS
# primitive loops: while & fo loops

# import math
import math

# while loop
# With the while loop we can execute a set of statements as long as a condition is true.
# num = 1000000; counting from 1000000 to 1 was done in 10:42:23
# A whole 10 minutes and 42 secs!! Never try this
# Same code using while loop in javascript takes 04:40:22 in browser
# Same code using while loop in javascript takes 16 seconds in nodejs
# counting 1Billion in nodejs takes 
num = 10
while num > 0:
    print(num)
    num-=1
# With the else statement we can run a block of code once when the condition no longer is true:
else:
    print("STOP COUNTING")


# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in range(10):
    print(i)



questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}.')
pow(3,4)


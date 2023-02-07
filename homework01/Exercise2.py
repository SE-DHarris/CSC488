#Python script 2:Using nested for loops and if statements, write a program that iterates over every integer from 3 to 100 (inclusive) and prints out the number only if it is a prime number.

for start in range(3, 101):
    for i in range(2, start):
        if (start % i) == 0:
         break
    else: 
         print(str(start) + " is prime")
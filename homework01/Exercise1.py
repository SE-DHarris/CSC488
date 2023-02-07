
import random

#Create list

numList = [2,30,12,32,50,45,67,57,92,51] 

for x in range(len(numList)):
    if(numList[x] % 2 == 1):
     print(str(numList[x]) + " is odd")
    else:
     print(str(numList[x]) + " is even")
'''Given an integer,N , perform the following conditional actions:
If N is odd, print Weird
If N is even and in the inclusive range of (2,5) , print Not Weird
If N is even and in the inclusive range of (6,20), print Weird
If N is even and greater than 20, print Not Weird'''

#!/bin/python3

N =  int(input())

if(N%2!=0):
    print("Weird")
elif(N%2==0):
    if(N in range(2,5)):
        print("Not Weird")
    elif(N in range(6,21)):
        print("Weird")
    elif(N>20):
        print("Not Weird")

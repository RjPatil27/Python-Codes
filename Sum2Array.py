'''Write a program to add the corresponding elements of two arrays, 
each of size N and print the sums. N can be any integer between 1 and 100. '''

N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

for i in range(0,N):
    sumArray.append(numArray1[i]+numArray2[i])

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")

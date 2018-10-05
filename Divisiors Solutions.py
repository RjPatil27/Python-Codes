'''Create a program that asks the user for a number
and then prints out a list of all the divisors of that number.'''

num = int(input("Enter Number: "))
divisorList = []
for i in list(range(1,num+1)):
    if num%i==0:
        divisorList.append(i)

print(divisorList)

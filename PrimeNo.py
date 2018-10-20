# Python Program - Check Prime Number or Not

print("Enter 'x' for exit.")
num = input("Enter any number: ")
if num == 'x':
    exit();
try:
    number = int(num)
except ValueError:
    print("Please, enter a number...exiting...")
else:
    for i in range(2, number):
    	if number%i == 0:
    	    print(number, "is not a prime number.")
    	    break;
    else:
        print(number, "is a prime number.")
		break;

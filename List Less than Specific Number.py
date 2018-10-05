'''
Take a specific list of type
a = [1, 1, 2, 3, 5, 8, 13]
then take one number and print all the numbers from list which are less than that number 
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(raw_input("Choose a number: "))

new_list = []

for i in a:
	if i < num:
		new_list.append(i)

print new_list

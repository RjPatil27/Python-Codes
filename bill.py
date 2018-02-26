#Python program for calculating bill of restaurant with tax and with tip also.

def tax(bill):
	bill*=1.08
	print("meal with tax:%f"%bill)
	return bill

def tip(bill):
	bill*=1.15
	print("meal with tip:%f"%bill)
	return bill

meal_cost=100
meal_with_tax=tax(meal_cost)
meal_with_tip=tip(meal_with_tax)

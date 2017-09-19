# Recitation Lab 3 Question 1: Program to calculate discounted price
# Author: Asmit De
# Date: 02/02/2017

item = input('Enter name of item: ')
cost = float(input('Enter cost of item: '))
discount = float(input('Enter the discount percentage: '))

finalprice = cost - cost * discount / 100

print('After discount', item, 'can be purchased for', finalprice)
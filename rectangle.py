'''
Rectangle Pattern
Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the 
number of rows (length) and m represents the number of columns (breadth).
'''

n=int(input("Enter the number n: "))
m=int(input("Enter the number m: "))
list1=[]
for i in range(n):
        list1.append('*'*m)
print(list1)
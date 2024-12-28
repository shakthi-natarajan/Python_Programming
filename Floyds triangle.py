'''
Floyds Triangle
Problem Description:
You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle 
is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, 
and so on.
Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in Floyd's Triangle.
'''

num=int(input('Enter a number: '))
counter=0
string1=''
list1=[]
for i in range(1, num+1):
    for j in range(i):
        counter+=1
        string1+=str(counter)+' '
    list1.append(string1)
    string1=''
print(list1)
'''
Diamond Pattern
Problem Description:
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars),
and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.
Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in the diamond pattern.
'''


num=int(input('Enter a number: '))
list1=[]
min=max=0
max=2*num-1
counter=1
for i in range(num):
    min=counter
    spaces=(max-min)//2
    string1=' '*spaces+'*'*counter+' '*spaces
    list1.append(string1)
    counter+=2
list2=list1[::]
list1.reverse()
list1.pop(0)
list1=list2+list1
for element in list1:
    print(element)

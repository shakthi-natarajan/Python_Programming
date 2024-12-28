

#printing hollow square
'''
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).
'''

num=int(input("Enter the number n: "))
list1=[]
hollow=num-2
for i in range(num):
    if i==0 or i==num-1:
        list1.append('*'*num)
    else:
        list1.append('*'+' '*hollow +'*')
print(list1)
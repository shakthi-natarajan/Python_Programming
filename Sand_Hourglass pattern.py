'''
Function to return a sandglass pattern of '*' of side n as a list of strings.
Parameters:n (int): The height of the sandglass.
Returns:list: A list of strings where each string represents a row of the sandglass pattern.
'''

def generate_sandglass(n):
    list1=[]
    max=2*n-1
    counter=max
    for i in range(n,0,-1):
        spaces=(max-counter)//2
        string1=' '*spaces+ '*'*counter+ ' '*spaces
        list1.append(string1)
        counter-=2

    list2=list1[::]
    list1.reverse()
    list1.pop(0)
    list1=list2+list1
    return list1
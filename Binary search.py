#Binary search
def binary_search(list1, target):
    start=0
    end=len(list1)-1
    while start<=end:
        middle=(start+end)//2
        if target<list1[middle]:
            end= middle-1
        elif target>list1[middle]:
            start=middle+1
        elif target==list1[middle]:
            return middle
    return -1

list1=[56,67,80,90,234]
print(binary_search(list1,67))
print(binary_search(list1,234))
print(binary_search(list1,300))
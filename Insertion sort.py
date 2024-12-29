#Insertion sort
def insertion_sort(lst):
    length=len(lst)
    for i in range(0,length-1):
        new=i+1
        for j in range(new,0,-1):
            if lst[j] < lst[j-1]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
            else:
                break
    print(lst)

insertion_sort([12,25,11,34,90,22])
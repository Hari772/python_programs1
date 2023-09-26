# to get currect position of pivot
def pivot_place(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left=left+1
        while left<=right and list1[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
        list1[first],list1[right]=list1[right],list1[first]
        return right # Here we will get the correct position of pivot
def quicksort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
list1=[56,26,93,17,31,44]
last=len(list1)
quicksort(list1,0,last-1)
print("sorted list:",list1)

    

            

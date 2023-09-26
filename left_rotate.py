n=int(input("Enter the number of array elements:"))
l=list(map(int,input().split()))
x=int(input("No of word to be trimmed: "))
a=l[ :x]
#print("array a is: ",a)
b=l[x: ]
#print("array b is: ",b)
c=b+a
print("new array is: ",c)

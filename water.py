print("x is jug having capacity 4 liters")
print("y is jug having capacity 3 liters")
x=int(input("Enter the initial capacity of jug x:"))
y=int(input("Enter the initial capacity of jug y:"))
for i in range(1,7):
    if i==0:
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==1:
        x=x+4
        y=y+3
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==2:
        x=x-4
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==3:
        x=x+y
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==4:
        x=x+(4-y)#x=4
        y=y-1#2
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==5:
        x=4-x
        print("x=",x,end=' ')
        print("y=",y)
        continue
    elif i==6:
        x,y=y,x
        print("x=",x,end=' ')
        print("y=",y)
        continue
if x==2:
    print("The required output is...")
    print("X=",x,end=" ")
    print("y=",y)    
        
 
        





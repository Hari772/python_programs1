
# minimum moves are (2**n)-1
def hanoi(n,sourse,desti,middle):
    if n<1:
        print("case is not possible")
        
    if n==1:
        print(f"move disk {n} from {sourse} to {desti}")
        return
    else:
        hanoi(n-1,sourse,middle,desti)
        print(f"move disk {n} from {sourse} to {desti}")
        hanoi(n-1,middle,desti,sourse)
n=int(input("Entre the number of disks:"))
hanoi(n,'A','C','B')
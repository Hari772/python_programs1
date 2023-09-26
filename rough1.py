
year=int(input("Enter the value of year:"))
def is_leap():
    if((year%400==0)or(year%100!=0)and(year%4==0)):
        print("True")
    else:
        print("False")
is_leap()



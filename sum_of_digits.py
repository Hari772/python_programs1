a=int(input("Enter the number:...."))
N=a
sum_of_digit=0
while N>0:
    digit=N%10
    sum_of_digit=sum_of_digit+digit
    N=N//10
print("Sum of digits=",sum_of_digit)
x=sum_of_digit
new_sum=0
if sum_of_digit>9:
    while x>0:
        new_digit=x%10
        new_sum=new_sum+new_digit
        x=x//10
    print("new_sum is",new_sum)
else:
    pass

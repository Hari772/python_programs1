s=input()
high=-999
for i in s:
    if i in "AEIOUaeiou":
        temp=s.count(i)#first repeating-> temp>high
        if temp>=high:#last repeating=temp>=high
            high=temp
            result=i
print(result)
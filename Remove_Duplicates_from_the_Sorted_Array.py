def duplicate(nums):
    l=[]
    c=0
    for i in nums:
        if i not in l:
            c=c+1
            l.append(i)
    l.sort()
    print(c)
    print(l)
nums=list(map(int,input().split(',')))
duplicate(nums)
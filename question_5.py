# a=list(map(int,input().strip().split()))
# s=''
# print(a)

# # for i in a.sort():
# #     s=s+str(i)
# # print(s)
c=input()
l=list(c)
s=''
l.sort()
for i in l:
    s=s+str(i)
print(s)
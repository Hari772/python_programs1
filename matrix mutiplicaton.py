# A=[[1,2,3],[1,2,3],[1,2,3]]
# B=[[1,2,3],[1,2,3],[1,2,3]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):#i=3,i=0,1,2
#     for j in range(len(B[0])):#j=3,j=0,1,2,
#                    for k in range(len(B)):#k=3,k=0,1,2
#                         result[i][j]+=A[i][k]*B[k][j]
# for  r in result:
#        print(r)

'''A=[[1,2,3],[1,2,3],[1,2,3]]
B=[[1,2,3],[1,2,3],[1,2,3]]
#multiply()
import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]])
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
res=np.multiply(a,b)
print("Matrix multiplication is:")
print(res)'''

# #using matmul()
# import numpy as np
# a=np.array([[1,2,3],[1,2,3],[1,2,3]])
# b=np.array([[1,2,3],[1,2,3],[1,2,3]])
# c=np.matmul(a,b)
# print("matrix multiplication is:")
# print(c)
 

''' using dot function'''
import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]])
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
c=np.dot(a,b)
print("matrix multiplication is:")
print(c)

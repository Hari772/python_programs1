# A=[[1,2,3],[4,5,6],[7,8,9]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i  in range(len(A)):
#     for j in range(len(A[0])):
#         result[j][i]=A[i][j]
# print("The transpose of a matrix is")
# for i in result:
#     print(i)


''' transpose()'''
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
res=np.transpose(a)
print("Transpose of matrix a is:  ")
print(res)

# syntax --> numpy.transpose(array,axis=None)

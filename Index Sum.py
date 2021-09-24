N = int(input())
A = []
for i in range(N):
    A.append(float(input()))
print(A)
M = int(input())
IND =[]
for j in range(M):
    IND.append(int(input()))
print(IND)
index_sum = 0
for el in IND:
    index_sum += A[el]
print(index_sum)

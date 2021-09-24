n = (int(input()))
A = []
for el in range(n):
    A.append(float(input()))

B = []
for i in range(len(A)):
    new_sum = 0
    for j in range(i, len(A)):
        new_sum += A[j]
    B.append(new_sum)
print(B)

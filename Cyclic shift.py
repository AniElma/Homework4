N = int(input())
k = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
print(lst)
for el in range(k):
    x = lst.pop()

    lst.insert(0, x)
print(lst)
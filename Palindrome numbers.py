
def palindrom(n):
    n_str = str(n)
    reverse = n_str[-1::-1]
    if n_str == reverse:
        return True
a = int(input())
b = int(input())

for i in range(a, (b+1)):
    if palindrom(i):
        print(i)




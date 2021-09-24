def prime(n):
    prime = True
    for el in range(2, n//2):
        if n % el == 0:
           prime = False
           break
    return prime


number = int(input())
for i in range(2, number//2+1):
    if prime(i) and prime(number - i):
        print(i, number-i)
        break



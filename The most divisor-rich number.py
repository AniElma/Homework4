def most_divisors(n):
    number_of_divisors = 0
    for el in range(1, (n+1)):
     if n % el == 0:
      number_of_divisors += 1
    return(number_of_divisors)


a = int(input())
b = int(input())
max_divisors_rich = a

for number in range(a, b):
    if most_divisors(number) > most_divisors(max_divisors_rich):
     max_divisors_rich = number
print(max_divisors_rich)


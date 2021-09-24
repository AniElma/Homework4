def star_line(n):
    for i in range(1, n + 1, 2):
        spaces = int(((n - i) / 2)) * ' '
        star = '*' * i
        print(spaces +star)


number = int(input())
star_line(number)

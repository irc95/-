n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break

print()
input("Нажмите Enter")
a = list(map(int, input('Введите массив: ').split()))
m = sorted(a)[len(a) // 2] # Медиана 
print('Минимальное количество ходов:', sum(abs(v - m) for v in a)) # Кол-ва шагов для всего массива.
input("Нажмите ENTER")
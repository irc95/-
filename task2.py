import math
 
print("Введите координаты точки: ")
x = float(input("x = "))
y = float(input("y = "))
print("Введите центр окружности и его радиус: ")
r = float(input("R = "))
xk = float(input("x(k) = "))
yk = float(input("y(k) = "))


ellipse_equation = (x - xk)**2 / r**2 + (y - yk)**2 / r**2   # Уравнение эллипса, eсли это выражение меньше 1, то точка находится в окружности
 
 
if ellipse_equation < 1:
    print("Точка принадлежит кругу")
elif ellipse_equation == 1:
    print("Точка лежит на окружности")
else:
    print("Точка не принадлежит кругу")

input("Нажмите ENTER чтобы продолжить")
# 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
x = int(input("Введи координату Х "))
y = int(input("Введи координату Y "))

if x == 0:
    print("Ось у")
elif y == 0:
    print("Ось х")
elif x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y > 0:
    print("4")

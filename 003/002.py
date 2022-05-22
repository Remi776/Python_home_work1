# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

a_x, a_y = int(input('Ax = ')), int(input('Ay = '))
b_x, b_y = int(input('Bx = ')), int(input('By = '))
from math import sqrt, pow
distance = sqrt(pow(b_y - a_y, 2) + pow(b_x - a_x, 2))
print(f'A({a_x}, {a_y}); B({b_x}, {b_y}) -> {round(distance, 2)}')
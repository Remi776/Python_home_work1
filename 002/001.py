
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = int(input('X = ')), int(input('Y = ')), int(input('Z = '))
if not(x and y and z) == (not x) or (not y) or (not z):
    print('True')
else:
    print('False')
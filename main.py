 # Нарисовать квадратик со звездочек (пользователь вводит диагональ)
#легкое
diagonal = int(input("Введите длину диагонали: "))

for i in range(diagonal):
    for j in range(diagonal):
        if i == 0 or i == diagonal - 1 or j == 0 or j == diagonal - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#cреднее

# Нарисовать ромб со звездочек(пользователь вводит диагональ)

diagonal = int(input("Введите длину диагонали: "))

for i in range(diagonal):
    for j in range(diagonal):
        if i <= diagonal // 2:
            if j >= diagonal // 2 - i and j <= diagonal // 2 + i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j >= diagonal // 2 - (diagonal - 1 - i) and j <= diagonal // 2 + (diagonal - 1 - i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

#сложное

# Нарисовать не заполненный квадрат с заполненными диагоналями внутри
# Все с использованием только цикла for

size = int(input("Введите размер квадрата: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or j == size - 1 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

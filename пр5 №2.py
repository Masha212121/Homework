import matplotlib.pyplot as plt
import numpy as np


def draw_circle(center, radius):
    circle = plt.Circle(center, radius, color='blue', fill=False)
    plt.gca().add_artist(circle)


def check_point_position(center, radius, point):
    distance_squared = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return "точка находится внутри окружности"
    elif distance_squared == radius_squared:
        return "точка лежит на окружности"
    else:
        return "точка располагается за пределами окружности"


# Запрашиваем данные у пользователя
center_x = float(input("Введите координату X центра окружности: "))
center_y = float(input("Введите координату Y центра окружности: "))
radius = float(input("Введите радиус окружности: "))
point_x = float(input("Введите координату X точки: "))
point_y = float(input("Введите координату Y точки: "))

center = (center_x, center_y)
point = (point_x, point_y)

# Строим окружность и точку
draw_circle(center, radius)
plt.plot(point[0], point[1], 'ro')  # 'ro' - красная точка
plt.xlim(center_x - radius - 1, center_x + radius + 1)
plt.ylim(center_y - radius - 1, center_y + radius + 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("Окружность и точка")
plt.show()

# Проверяем положение точки
result = check_point_position(center, radius, point)
print(result)
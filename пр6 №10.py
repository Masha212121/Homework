def rectangles_relative_position(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    if x1_1 < x2_2 and x2_1 > x1_2 and y1_1 > y2_2 and y2_1 < y1_2:
        if x1_1 >= x1_2 and x2_1 <= x2_2 and y1_1 <= y1_2 and y2_1 >= y2_2:
            return "Один прямоугольник лежит внутри другого, не касаясь."
        elif x1_2 >= x1_1 and x2_2 <= x2_1 and y1_2 <= y1_1 and y2_2 >= y2_1:
            return "Один прямоугольник лежит внутри другого, не касаясь."
        else:
            return "Прямоугольники имеют пересечение."
    elif x1_1 == x2_2 or x2_1 == x1_2 or y1_1 == y2_2 or y2_1 == y1_2:
        return "Прямоугольники имеют касание."
    else:
        return "Прямоугольники лежат вне друг друга, не касаясь."

x1_1 = float(input("Введите x-координату верхней левой вершины первого прямоугольника: "))
y1_1 = float(input("Введите y-координату верхней левой вершины первого прямоугольника: "))
x2_1 = float(input("Введите x-координату правой нижней вершины первого прямоугольника: "))
y2_1 = float(input("Введите y-координату правой нижней вершины первого прямоугольника: "))

x1_2 = float(input("Введите x-координату верхней левой вершины второго прямоугольника: "))
y1_2 = float(input("Введите y-координату верхней левой вершины второго прямоугольника: "))
x2_2 = float(input("Введите x-координату правой нижней вершины второго прямоугольника: "))
y2_2 = float(input("Введите y-координату правой нижней вершины второго прямоугольника: "))

result = rectangles_relative_position(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2)
print(result)
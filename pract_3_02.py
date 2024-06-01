# Увести з клавіатури координати двох точок А (х1, у1) і В (х2, у2). Скласти алгоритм, який визначає, яка з точок знаходиться ближче до початку координат.

def distance_from_origin(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def closer_point():
    x1 = float(input("Введіть координату x для точки А: "))
    y1 = float(input("Введіть координату y для точки А: "))
    x2 = float(input("Введіть координату x для точки В: "))
    y2 = float(input("Введіть координату y для точки В: "))

    distance_a = distance_from_origin(x1, y1)
    distance_b = distance_from_origin(x2, y2)

    if distance_a < distance_b:
        print("Точка А знаходиться ближче до початку координат.")
    elif distance_b < distance_a:
        print("Точка В знаходиться ближче до початку координат.")
    else:
        print("Точки А і В знаходяться на однаковій відстані від початку координат.")

closer_point()

# На площині ХОY задана своїми координатами точка А (координати 
# ввести з клавіатури). Вказати, де вона розташована (на якій осі або в якому 
# координатном куті).

def locate_point(x, y):
    if x == 0 and y == 0:
        print("Точка розташована в початку координат.")
    elif x == 0:
        print("Точка розташована на вісі Y.")
    elif y == 0:
        print("Точка розташована на вісі X.")
    elif x > 0 and y > 0:
        print("Точка розташована в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка розташована в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка розташована в третьому квадранті.")
    elif x > 0 and y < 0:
        print("Точка розташована в четвертому квадранті.")

def main():
    x = float(input("Введіть координату x для точки А: "))
    y = float(input("Введіть координату y для точки А: "))

    locate_point(x, y)

main()
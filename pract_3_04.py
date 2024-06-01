# Увести з клавіатури дійсні числа х і у, не рівні одне одному. Менше з цих 
# двох чисел замінити половиною їх суми, а більше - їх подвоєним добутком.

def replace_numbers(x, y):
    if x != y:
        if x < y:
            smaller = x
            greater = y
        else:
            smaller = y
            greater = x

        x = (smaller + greater) / 2
        y = smaller * greater * 2

        return x, y
    else:
        print("Помилка: Введені числа рівні одне одному.")
        return None, None

def main():
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))

    new_x, new_y = replace_numbers(x, y)

    if new_x is not None and new_y is not None:
        print("Після заміни:")
        print("x =", new_x)
        print("y =", new_y)

main()

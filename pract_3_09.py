# Підрахувати кількість цілих серед чисел а, b, с (ввести з клавіатури).

def count_integer_numbers(a, b, c):
    count = 0
    if a.is_integer():
        count += 1
    if b.is_integer():
        count += 1
    if c.is_integer():
        count += 1
    return count

def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    integer_count = count_integer_numbers(a, b, c)

    print("Кількість цілих чисел серед a, b, c:", integer_count)

main()

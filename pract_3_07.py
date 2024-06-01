#  Підрахувати кількість негативних серед чисел а, b, с (ввести з клавіатури).

def count_negative_numbers(a, b, c):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    negative_count = count_negative_numbers(a, b, c)

    print("Кількість негативних чисел серед a, b, c:", negative_count)

main()

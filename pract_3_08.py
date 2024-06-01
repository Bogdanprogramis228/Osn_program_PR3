# Підрахувати кількість додатних серед чисел а, b, с (ввести з клавіатури).

def count_positive_numbers(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    return count

def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    positive_count = count_positive_numbers(a, b, c)

    print("Кількість додатніх чисел серед a, b, c:", positive_count)

main()

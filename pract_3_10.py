# Визначити, дільником яких чисел а, b, с є число k (ввести з клавіатури).

def is_divisor_of_numbers(a, b, c, k):
    if a % k == 0:
        print(f"{k} є дільником числа {a}.")
    else:
        print(f"{k} не є дільником числа {a}.")

    if b % k == 0:
        print(f"{k} є дільником числа {b}.")
    else:
        print(f"{k} не є дільником числа {b}.")

    if c % k == 0:
        print(f"{k} є дільником числа {c}.")
    else:
        print(f"{k} не є дільником числа {c}.")

def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k (дільник): "))

    is_divisor_of_numbers(a, b, c, k)

main()

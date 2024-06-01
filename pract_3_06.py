# Увести з клавіатури цілі числа a, b. Якщо числа не рівні, то замінити кожне з них одним і тим же числом, рівним більшому із вихідних, а якщо рівні, тозамінити числа нулями.

def modify_numbers(a, b):
    if a != b:
        result = max(a, b)
    else:
        result = 0
    return result

def main():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))

    modified_number = modify_numbers(a, b)

    print("Після заміни:")
    print("a =", modified_number)
    print("b =", modified_number)

main()

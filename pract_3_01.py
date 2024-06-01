# Увести з клавіатури три дійсних числа. Піднести до квадрата ті з них, 
# значення яких невід'ємні, і в четверту ступінь - від`ємні .


def square_or_fourth_power():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))

    result = []
    for num in [num1, num2, num3]:
        if num >= 0:
            result.append(num ** 2)
        else:
            result.append(num ** 4)

    print("Результат:")
    for i, res in enumerate(result, 1):
        print(f"Число {i}: {res}")

square_or_fourth_power()

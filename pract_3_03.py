# Увести з клавіатури величини двох кутів трикутника (в градусах). 
# Визначити, чи існує такий трикутник, і якщо так, то чи буде він прямокутним.

import math

def is_triangle_possible(angle1, angle2):
    if angle1 + angle2 < 180:
        return True
    else:
        return False

def is_right_triangle(angle1, angle2):
    if angle1 == 90 or angle2 == 90:
        return True
    else:
        return False

def main():
    angle1 = float(input("Введіть величину першого кута трикутника (в градусах): "))
    angle2 = float(input("Введіть величину другого кута трикутника (в градусах): "))

    if is_triangle_possible(angle1, angle2):
        print("Так, цей трикутник існує.")
        if is_right_triangle(angle1, angle2):
            print("Цей трикутник є прямокутним.")
        else:
            print("Цей трикутник не є прямокутним.")
    else:
        print("Цей трикутник не існує.")

main()

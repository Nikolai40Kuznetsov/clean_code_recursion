# Main file of the project
# All rights are reserved

# Import all nesessary libs and modules
import Euclid as E
import Packal as P
from distant_module import notation as n

# The main function of the project
def main():
    user_choise = int(input("Выберите функцию, которую хотите использовать: "))
    if user_choise == 1:
        number_1 = input("Введите первое число ")
        number_2 = input("Введите второе число ")
        print(f"Их наибольший общий делитель: {E.Euclid(int(number_1), int(number_2))}")
    if user_choise == 2:
        level = input("Введите уровень треугольника Паскаля ")
        triangle = P.Packals_triangle(int(level))
        for row in triangle:
            print(row)
    if user_choise == 3:
        number = int(input("Введите число "))
        base = int(input("Введите базу системы счисления "))
        print(f"Число {number}, записанное в десятичной системе, в системе с основанием {base} записывется как {n.transfer(number, base)}")

if __name__ == "__main__":
    main()
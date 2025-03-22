
# try:
#     print(10 / 2)
#     print("програма продовжує працювати")
# except ZeroDivisionError:
#     print("Не можливо ділити на 0")
# except ArithmeticError:
#     print("Виникла арифметична помилка")
#
# print("програма продовжує працювати")


# class BuildingError(Exception):
#     def __str__(self):
#         return f"З такою кількістью матеріалів не можливо будувати будинок"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material>limit_value:
#         return "Достатньо материалів"
#     else:
#         raise BuildingError(amount_of_material)
#
# material = 123
# check_material(material, 300)


# try:
#     numerator = int(input("Введіть чисельник: "))
#     denominator = int(input("Введіть знаменник: "))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка : Ділення на ноль неможливе")
#
# except ValueError:
#     print("Помилка : Введені данні не є числом")

import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
try:
    warnings.warn("Warning, module not import", ImportWarning)
except Exception:
    print("Warning")

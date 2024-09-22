from comlex_number import ComplexNumber
from operations import AddOperation, MultiplyOperation, DivideOperation
from logger import logger

def get_complex_number():
    real = float(input("Введите действующую часть: "))
    imag = float(input("Введите мнимую часть: "))
    return ComplexNumber(real, imag)

def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Умножение")
        print("3. Деление")
        print("4. Выход")

choice = input("Введите номер операции: ")

if choice == '1':
    num1 = get_complex_number()
    num2 = get_complex_number()
    operation = AddOperation()
    result = operation.execute(num1, num2)
    logger.info(f"Сложение: {num1} + {num2} = {result}")
    print(f"Результат: {result}")
elif choice == '2':
    num1 = get_complex_number()
    num2 = get_complex_number()
    operation = DivideOperation()
    result = operation.execute(num1, num2)
    logger.info(f"Умножение: {num1} * {num2} = {result}")
    print(f"Результат: {result}")
elif choice == '3':
    num1 = get_complex_number()
    num2 = get_complex_number()
    operation = DivideOperation()
    result = operation.execute(num1, num2)
    logger.info(f"Деление: {num1} / {num2} = {result}")
    print(f"Результат: {result}")
elif choice == '4':
    break
else:
    print("Неверный ввод!")

if __name__ =="__main__":
    main()
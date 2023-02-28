def add(x: float, y: float):
    return x + y


def subtract(x: float, y: float):
    return x - y


def multiply(x: float, y: float):
    return x * y


def divide(x: float, y: float):
    return x / y


def main():
    while True:
        choice = input("Choose operation (+, -, *, /): ")

        if choice in '+-*/':
            try:
                operand_1 = float(input("First operand: "))
                operand_2 = float(input("Second operand: "))
            except ValueError:
                print("Not a number.")
                continue

            if choice == '+':
                print(f'{operand_1} + {operand_2} = {add(operand_1, operand_2)}')
            elif choice == '-':
                print(f'{operand_1} - {operand_2} = {subtract(operand_1, operand_2)}')
            elif choice == '*':
                print(f'{operand_1} * {operand_2} = {multiply(operand_1, operand_2)}')
            elif choice == '/':
                print(f'{operand_1} / {operand_2} = {divide(operand_1, operand_2)}')


if __name__ == "__main__":
    main()

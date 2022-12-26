from art import logo

print(logo)

# def math ops and dict of operations for ref in code later


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divid(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divid,
}


def calulator():
    cont = 'y'
    num1 = float(input('what is the first number?\n'))

    while cont == 'y':
        for op in operations:
            print(op)
        operation_symbol = input(
            "pick and operation symbol from the line above\n")
        num2 = float(input('what is the next number?\n'))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        num1 = result
        cont = input(
            f"type 'y' to continue with {result} to exit type 'n'\n").lower()
    calulator()


calulator()

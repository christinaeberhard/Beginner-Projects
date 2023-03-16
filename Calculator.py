from calc import logo

""" Functions to ... Add / Substract / Multiply / Divide """
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


""" create a dict named operations with key = +-*/ and values = functions """
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = input("Please pick an operator: ")
        num2 = float(input("What is the next number?: "))

        for result in operations:
            if result == operator:
                function = operations[result]
                answer = function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
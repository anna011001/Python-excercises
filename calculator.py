def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    should_accumulate = True
    num1 = float(input("Type first number: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation = input("Type operation: ")

        num2 = float(input("Type second number: "))
        
        if operation in operations:
            result = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")
                
        print("Do you want to continue working with the previous result? Type 'yes' or 'no'.")
        continue_calculating = input()
        if continue_calculating == "yes":
            num1 = result
        else:
            should_accumulate = False
            calculator()

calculator()
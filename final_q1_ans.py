def rpn(calc):
    stack = []
    operators = ['+', '-', '*', '/']

    for token in calc:
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == operators[0]:
                stack.append(operand1 + operand2)
            elif token == operators[1]:
                stack.append(operand1 - operand2)
            elif token == operators[2]:
                stack.append(operand1 * operand2)
            elif token == operators[3]:
                if operand2 != 0:
                    stack.append(int(operand1 / operand2))
                else:
                    print("Divide by 0.")
                    return None

    return stack[0]

#calc = ["3", "4", "*", "10", "2", "/", "+"]
calc = ["5", "9", "5","*", "25", "-", "*"]
print(rpn(calc))

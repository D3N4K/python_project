def valid_brack(string):
    stack = []
    valid = True
    for i in string:
        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if len(stack) == 0:
                valid = False
                break
            brack = stack.pop()
            if (brack == '(' and i == ')') or (brack == '[' and i == ']') or (brack == '{' and i == '}'):
                continue
            else:
                valid = False
                break
    if valid and len(stack) == 0:
        return 'верно'
    else:
        return 'неверно'
def task_of_brackets(brackets_string):
    print(brackets_string, '-', valid_brack(brackets_string))
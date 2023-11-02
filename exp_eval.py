from stack_array import Stack
#changes made
# You do not need to change this class
class PostfixFormatException(Exception):
    pass

operators = ["*", "+", "-", "/", "**", "<<", ">>"]
presendece = {"<<" : 3, ">>": 3, "**": 2, "*": 1, "/": 1, "+": 0, "-": 0}
def eval(second, first, operator):
    if operator == "*":
        return (float(first) * float(second))
    if operator == "+":
        return (float(first) + float(second))
    if operator == "-":
        return (float(first) - float(second))
    if operator == "/":
        if float(second) == 0:
            raise ValueError
        else:
            return (float(first) / float(second))
    if operator == "**":
        return (float(first) ** float(second))
    if operator == "<<":
        try:
            return(int(first) << int(second))
        except:
            raise PostfixFormatException('Illegal bit shift operand')
    if operator == ">>":
        try:
            return (int(first) >> int(second))
        except:
            raise PostfixFormatException('Illegal bit shift operand')
def check_validity(input_str):
    if input_str == "" or input_str.split() == []:
        raise PostfixFormatException("Empty input")
    num_count = 0
    operand_count = 0
    input_list = input_str.split()
    for val in input_list:
        if val in operators:
            operand_count += 1
        else:
            try:
                float(val)
                num_count +=1
            except:
                raise PostfixFormatException("Invalid token")

    if num_count - operand_count >=2 :
        raise PostfixFormatException("Too many operands")
    if num_count <= operand_count:
        raise PostfixFormatException("Insufficient operands")
def postfix_eval(input_str):
    '''Evaluates a postfix expression

    Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack(30)
    check_validity(input_str)
    input_list = input_str.split()
    for val in input_list:
        try :
            float(val)   #check if it's a number and pushes it
            stack.push(val)
        except:
            if val in operators:  #if it's not check if its an operator
                stack.push(eval(stack.pop(), stack.pop(), val)) #do operation and push to stack
    return_val = stack.pop() #get last value in stack
    if int(return_val) == float(return_val):
        return int(return_val)
    else:
        return float(return_val)

def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    running_string = ""
    input_list = input_str.split()
    stack = Stack(30)
    for val in input_list:
        try:
            float(val)              #check if its a number
            if running_string == "":
                running_string += val
            else:
                running_string +=f' {val}'   #append it
        except ValueError:
            if val == "(":          #if its open parethesis push it to the stack
                stack.push(val)
            if val == ")":          #if its a closed parenthesis
                closed_p = False
                while closed_p == False: #keep popping and appending until closed paretnhesis
                    last = stack.pop()
                    if last == "(":
                        closed_p == True
                        break
                    else:
                        running_string += f' {last}'
            if val in operators and stack.size() > 0:            #if its an operator and stack has something in it
                while (stack.size() > 0 and stack.peek() in operators) and \
                 ((val != "**" and presendece[val] <= presendece[stack.peek()]) \
                 or (val == "**" and presendece[val] < presendece[stack.peek()])):   #while the stack has something in it and
                    running_string += f' {stack.pop()}'                              #its an operator meeting the conditions,
                                                                # pop that operator from the stack and add it
                stack.push(val)
            if val in operators and stack.size() == 0:
                stack.push(val)
    for n in range(stack.size()):
        append_val = stack.pop()
        if append_val in operators:
            running_string += f' {append_val}'
    return running_string


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression

    Input argument:  a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    stack = Stack(30)
    input_list = input_str.split()
    input_list = input_list[::-1]
    for val in input_list:
        try:
            float(val)
            stack.push(val)
        except:
            if val in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                string = op1 + f" {op2}" + f" {val}"
                stack.push(string)
    return(stack.pop())


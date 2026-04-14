tokens = ['2', '+', '3', '-', '4']
pos = 0  # current position


def current_token():
    if pos < len(tokens):
        return tokens[pos]
    return None


def match(expected):
    global pos
    if current_token() == expected:
        print(f"Operator: {current_token()}")
        pos += 1
    else:
        # stop and raise
        raise Exception(f"Expected {expected}, got \"{current_token()}\" at {pos}th position")


def parse_number():
    global pos
    if current_token().isdigit():
        print("Number:", current_token())
        pos += 1
    else:
        raise Exception(f"Expected number, got \"{current_token()}\" at {pos}th position")

"""
# 2 operands
def parse_expression():
    parse_number()
    match('+')
    parse_number()
    print("Valid expression!")
"""
# > 2 operands
def parse_expression():
    print(f"Tokens given: {tokens}\n")
    parse_number()   # checking first token
    while current_token() in ['+','-']:
        op = current_token()
        match(op)       # if is operator => move to next token
        parse_number()  # if number => move to next loop (expect op)
    print("Valid expression!")

# run parser
parse_expression()
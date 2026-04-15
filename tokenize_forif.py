def tokenize(expr):
    tokens = []
    number = ""
    
    for ch in str(expr):
        if ch.isdigit():
            number += ch
        else:
            if number != "":            #first 2 if getting the number
                tokens.append(number)
                number = ""

            if ch in "+-*/()":
                tokens.append(ch)
            elif ch == " ":
                continue
            else:
                raise ValueError(f"Invalid character: {ch}")

    if number != "":    #the last number
        tokens.append(number)

    for i in range(len(tokens) - 1):
        if tokens[i] == '/' and tokens[i+1] == '0':
            raise ValueError("Division by zero detected!")

    return tokens

expr = "10*3 - 4/0"

print(tokenize(expr))


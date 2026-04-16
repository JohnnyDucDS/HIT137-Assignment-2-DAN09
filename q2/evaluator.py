import os


def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, int):
        return str(value)

    text = f"{value:.4f}"
    text = text.rstrip("0").rstrip(".")
    return text


def format_result(value):
    if isinstance(value, str):
        return value

    if float(value).is_integer():
        return str(int(value))

    return f"{value:.4f}"


def token_to_string(token):
    token_type, token_value = token

    if token_type == "END":
        return "[END]"

    return f"[{token_type}:{token_value}]"


def tokens_to_string(tokens):
    return " ".join(token_to_string(token) for token in tokens)


def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        ch = expression[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or ch == ".":
            start = i
            dot_count = 0

            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                if expression[i] == ".":
                    dot_count += 1
                i += 1

            number_text = expression[start:i]

            if dot_count > 1 or number_text == ".":
                raise ValueError("Invalid number")

            number_value = float(number_text)
            tokens.append(("NUM", format_number(number_value)))
            continue

        if ch in "+-*/":
            tokens.append(("OP", ch))
            i += 1
            continue

        if ch == "(":
            tokens.append(("LPAREN", ch))
            i += 1
            continue

        if ch == ")":
            tokens.append(("RPAREN", ch))
            i += 1
            continue

        raise ValueError("Invalid character")

    tokens.append(("END", ""))
    return tokens


def needs_implicit_multiplication(left_token, right_token):
    left_type = left_token[0]
    right_type = right_token[0]

    left_ok = left_type in ("NUM", "RPAREN")
    right_ok = right_type in ("NUM", "LPAREN")

    return left_ok and right_ok


def add_implicit_multiplication(tokens):
    new_tokens = []

    for i in range(len(tokens) - 1):
        current_token = tokens[i]
        next_token = tokens[i + 1]

        new_tokens.append(current_token)

        if needs_implicit_multiplication(current_token, next_token):
            new_tokens.append(("OP", "*"))

    new_tokens.append(tokens[-1])
    return new_tokens


def parse_expression(tokens, pos):
    left_node, pos = parse_term(tokens, pos)

    while pos < len(tokens) and tokens[pos][0] == "OP" and tokens[pos][1] in ("+", "-"):
        operator = tokens[pos][1]
        pos += 1
        right_node, pos = parse_term(tokens, pos)
        left_node = (operator, left_node, right_node)

    return left_node, pos


def parse_term(tokens, pos):
    left_node, pos = parse_factor(tokens, pos)

    while pos < len(tokens) and tokens[pos][0] == "OP" and tokens[pos][1] in ("*", "/"):
        operator = tokens[pos][1]
        pos += 1
        right_node, pos = parse_factor(tokens, pos)
        left_node = (operator, left_node, right_node)

    return left_node, pos


def parse_factor(tokens, pos):
    token_type, token_value = tokens[pos]

    if token_type == "OP" and token_value == "-":
        if pos == 0 or tokens[pos - 1][0] in ("OP", "LPAREN"):
            pos += 1
            operand, pos = parse_factor(tokens, pos)
            return ("neg", operand), pos
        raise ValueError("Invalid unary negation")

    if token_type == "OP" and token_value == "+":
        raise ValueError("Unary plus is not supported")

    if token_type == "NUM":
        return ("num", float(token_value)), pos + 1

    if token_type == "LPAREN":
        pos += 1
        node, pos = parse_expression(tokens, pos)

        if pos >= len(tokens) or tokens[pos][0] != "RPAREN":
            raise ValueError("Missing closing parenthesis")

        return node, pos + 1

    raise ValueError("Invalid syntax")


def tree_to_string(node):
    node_type = node[0]

    if node_type == "num":
        return format_number(node[1])

    if node_type == "neg":
        return f"(neg {tree_to_string(node[1])})"

    operator = node[0]
    left_text = tree_to_string(node[1])
    right_text = tree_to_string(node[2])

    return f"({operator} {left_text} {right_text})"


def evaluate_tree(node):
    node_type = node[0]

    if node_type == "num":
        return node[1]

    if node_type == "neg":
        return -evaluate_tree(node[1])

    operator = node[0]
    left_value = evaluate_tree(node[1])
    right_value = evaluate_tree(node[2])

    if operator == "+":
        return left_value + right_value
    if operator == "-":
        return left_value - right_value
    if operator == "*":
        return left_value * right_value
    if operator == "/":
        if right_value == 0:
            raise ZeroDivisionError("Division by zero")
        return left_value / right_value

    raise ValueError("Unknown operator")


def process_expression(expression):
    original_expression = expression.rstrip("\n")

    try:
        tokens = tokenize(original_expression)
        tokens = add_implicit_multiplication(tokens)

        tree, pos = parse_expression(tokens, 0)

        if tokens[pos][0] != "END":
            raise ValueError("Extra input after valid expression")

        result = evaluate_tree(tree)

        return {
            "input": original_expression,
            "tree": tree_to_string(tree),
            "tokens": tokens_to_string(tokens),
            "result": result
        }

    except Exception:
        return {
            "input": original_expression,
            "tree": "ERROR",
            "tokens": "ERROR",
            "result": "ERROR"
        }


def write_output_file(output_path, results):
    with open(output_path, "w", encoding="utf-8") as file:
        for index, item in enumerate(results):
            file.write(f"Input: {item['input']}\n")
            file.write(f"Tree: {item['tree']}\n")
            file.write(f"Tokens: {item['tokens']}\n")
            file.write(f"Result: {format_result(item['result'])}\n")

            if index != len(results) - 1:
                file.write("\n")


def evaluate_file(input_path: str) -> list[dict]:
    results = []

    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "":
                continue
            results.append(process_expression(line.rstrip("\n")))

    folder = os.path.dirname(input_path)
    output_path = os.path.join(folder, "output.txt") if folder else "output.txt"

    write_output_file(output_path, results)
    return results


if __name__ == "__main__":
    input_file = "q2/sample_input.txt"

    try:
        output = evaluate_file(input_file)
        print("Done. Results written to output.txt")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found in this folder.")
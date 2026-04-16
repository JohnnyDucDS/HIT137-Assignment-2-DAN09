# tokenizer.py

def format_number(num):
    if isinstance(num, int):
        return str(num)

    if isinstance(num, float) and num.is_integer():
        return str(int(num))

    text = f"{num:.4f}"
    text = text.rstrip("0").rstrip(".")
    return text


def token_to_string(token):
    kind, value = token

    if kind == "END":
        return "[END]"

    return f"[{kind}:{value}]"


def tokens_to_string(tokens):
    parts = []

    for token in tokens:
        parts.append(token_to_string(token))

    return " ".join(parts)


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

        raise ValueError(f"Invalid character: {ch}")

    tokens.append(("END", ""))
    return tokens


def needs_implicit_multiplication(left_token, right_token):
    left_type = left_token[0]
    right_type = right_token[0]

    left_ok = left_type in ("NUM", "RPAREN")
    right_ok = right_type in ("NUM", "LPAREN")

    return left_ok and right_ok


def add_implicit_multiplication(tokens):
    result = []

    for i in range(len(tokens) - 1):
        current_token = tokens[i]
        next_token = tokens[i + 1]

        result.append(current_token)

        if needs_implicit_multiplication(current_token, next_token):
            result.append(("OP", "*"))

    result.append(tokens[-1])
    return result


def generate_tokens(expression):
    basic_tokens = tokenize(expression)
    final_tokens = add_implicit_multiplication(basic_tokens)
    return final_tokens


def main():
    expression = "2(3+4) + 5.5 * 2"

    print("===== TOKENIZER OUTPUT =====")
    print("Program Name: tokenizer")
    print("----------------------------")
    print("Input Expression:")
    print(expression)

    try:
        tokens = generate_tokens(expression)

        print("\nRaw Tokens:")
        print(tokens)

        print("\nFormatted Tokens:")
        print(tokens_to_string(tokens))

    except Exception as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()
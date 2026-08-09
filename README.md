# Python Programming Projects

This repository contains two Python programs originally developed as part of a university programming assignment.

The projects demonstrate Python fundamentals including file handling, string processing, recursion, tokenization, parsing, validation, and algorithm design.

---

## 📁 Repository Structure

```text
python-programming-projects/
│
├── caesar_cipher/
│   ├── caesar_cipher.py
│   └── raw_text.txt
│
├── expression_parser/
│   ├── expression_parser.py
│   └── sample_input.txt
│
└── README.md
```

The output files are generated automatically when each program is run.

---

## 🔐 1. Caesar Cipher

The Caesar Cipher program reads text from an input file, encrypts the text using user-provided shift values, decrypts the encrypted result, and verifies that the decrypted text matches the original.

### Files

- `caesar_cipher.py` — main Python program
- `raw_text.txt` — sample text used as input
- `encrypted_text.txt` — generated encrypted output
- `decrypted_text.txt` — generated decrypted output

The encrypted and decrypted files are created automatically when the program is executed.

### Features

- Reads text from a file
- Accepts two shift values from the user
- Encrypts alphabetic characters
- Preserves non-alphabetic characters
- Writes encrypted text to a new file
- Decrypts the encrypted text
- Verifies that the decrypted result matches the original text

### ▶️ Run the Program

From the repository root:

```bash
cd caesar_cipher
python caesar_cipher.py
```

The program reads:

`raw_text.txt`

and generates:

`encrypted_text.txt`

`decrypted_text.txt`

### 🧠 Concepts Practised

- File input and output
- String manipulation
- `ord()` and `chr()`
- Conditional logic
- Functions
- Encryption and decryption algorithms
- Verification and testing

---

## 🧮 2. Expression Parser

The Expression Parser reads mathematical expressions from a text file and evaluates them using recursive descent parsing.

Each line in the input file contains one mathematical expression.

### Files

- `expression_parser.py` — main Python program
- `sample_input.txt` — sample mathematical expressions
- `output.txt` — generated results

The `output.txt` file is created automatically when the program is executed.

### Supported Expressions

The parser supports:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Parentheses
- Nested parentheses
- Unary negation
- Implicit multiplication
- Operator precedence

Example input:

```text
3 + 5
2 + 3 * 4
-(3 + 4)
--5
(10 - 2) * 3 + -4 / 2
3 @ 5
```

### Output

For each expression, the generated `output.txt` includes:

- Input expression
- Expression tree
- Tokens
- Calculated result

### ▶️ Run the Program

From the repository root:

```bash
cd expression_parser
python expression_parser.py
```

The program reads:

`sample_input.txt`

and creates:

`output.txt`

### 🧠 Concepts Practised

- Tokenization
- Recursive descent parsing
- Recursion
- Operator precedence
- Expression trees
- File processing
- Input validation
- Error handling
- Debugging edge cases

---

## 🧠 What I Learned

These projects helped strengthen my understanding of how Python programs process and transform data.

The cipher project gave me practical experience with file handling, character manipulation, reversible algorithms, and output verification.

The expression parser introduced more advanced programming concepts such as tokenization, recursive descent parsing, operator precedence, expression trees, and handling malformed input.

---

## 👥 Team and Contributions

This project was originally developed as a group university assignments.

### Team Members

- **Johnny / Duc** — Group leader; integration, final review and improvements
- **Thien Ton** — expression_parser/tree part
- **Vy** — caesar_cipher/encryption-decryption part
- **Tamin** — expression_parser/tokens part

Individual development work can also be seen in the project branches and Git commit history.

### My Contribution

As the group leader, I was involved in coordinating the project and integrating the team's work into the final submission.

My main contributions included:

- Verifying the decrypted_text and the original_text in the cipher code. Working, interacting with files in the parser project.
- Integrating work from different branches
- Reviewing and debugging the combined program
- Making adjustments to the final version
- Testing the final program and resolving integration issues
- Further improving and reorganising the project for this portfolio repository

---

## 📚 Project Background

These programs were originally developed as part of a university programming assignment and have been organised and documented here for portfolio and learning purposes.

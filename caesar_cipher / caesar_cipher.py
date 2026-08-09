
def encrypt_text(shift1, shift2):
    result = ""
    encrypt_method = ""

    with open("raw_text.txt", "r") as f:
        text = f.read()


    for char in text:
        # lowercase
        if char.islower():
            index = ord(char) - ord('a')    # Set the character to a range of 0-25 (position in alphabet) 

            if char <= 'm':
                shift = shift1 * shift2
                new_index = (index + shift) % 26
                encrypt_method += "1"       # for shift rule 1
            else:
                shift = shift1 + shift2
                new_index = (index - shift) % 26
                encrypt_method += "2"       # for shift rule 2

            result += chr(new_index + ord('a'))

        # uppercase
        elif char.isupper():
            index = ord(char) - ord('A')

            if char <= 'M':
                shift = shift1
                new_index = (index - shift) % 26
                encrypt_method += "3"       # for shift rule 3
            else:
                shift = shift2 ** 2
                new_index = (index + shift) % 26
                encrypt_method += "4"       # for shift rule 4

            result += chr(new_index + ord('A'))

        # other characters
        else:
            encrypt_method += "0"           # rule 0 - remain unchanged       
            result += char

    with open("cipher_code.txt", "w") as cc:
        cc.write(encrypt_method)
    with open("encrypted_text.txt", "w") as ec:
        ec.write(result)

    return result

"""
A helper file cipher_code.txt is used to store which rule was applied to each character during encryption. 
This ensures the decryption function can exactly reverse the original rule, 
since the encrypted character alone may not reveal whether 
the original character came from the first or second half of the alphabet.

"""


def decrypt_text(shift1, shift2):
    result = ""

    with open("cipher_code.txt", "r") as c:
        cipher = c.read()

    with open("encrypted_text.txt", "r") as e:
        encrypt = e.read()

    for i in range(len(encrypt)):
        char = encrypt[i]
        method = cipher[i]

        # lowercase
        if char.islower() and method == "1":
            index = ord(char) - ord('a')
            shift = shift1 * shift2
            new_index = (index - shift) % 26
            result += chr(new_index + ord('a'))

        elif char.islower() and method == "2":
            index = ord(char) - ord('a')
            shift = shift1 + shift2
            new_index = (index + shift) % 26
            result += chr(new_index + ord('a'))

        # uppercase
        elif char.isupper() and method == "3":
            index = ord(char) - ord('A')
            shift = shift1
            new_index = (index + shift) % 26
            result += chr(new_index + ord('A'))

        elif char.isupper() and method == "4":
            index = ord(char) - ord('A')
            shift = shift2 ** 2
            new_index = (index - shift) % 26
            result += chr(new_index + ord('A'))

        else:
            result += char

    with open("decrypted_text.txt", "w") as dc:
        dc.write(result)
    return result


def verify():
    with open("raw_text.txt", "r") as r:
        original = r.read()

    with open("decrypted_text.txt", "r") as d:
        decrypted = d.read()

    if original == decrypted:
        print("Decryption was successful")
    else:
        print("Decryption was not successful")
    

#-------------------------------------------------------------

if __name__ == "__main__":
    while True:
        try:
            shift1 = int(input("Enter shift1: "))
            shift2 = int(input("Enter shift2: "))
            break
        except ValueError:
            print("Error: Only integer is accepted")

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify()

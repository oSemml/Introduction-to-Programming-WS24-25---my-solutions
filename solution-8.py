def create_dict(shift):
    # Create a dictionary that maps each letter to its shifted counterpart
    code_dict = {}
    for letter in range(0, 26):
        shifted_letter = (letter + shift) % 26
        code_dict[chr(letter + 97)] = chr(shifted_letter + 97)
    return code_dict

def encrypt(input_text):
    # Encrypt the input text by shifting each letter
    shift = 10
    code_dict = create_dict(shift)
    result = []
    for letter in input_text:
        result.append(code_dict[letter])
    return ''.join(result)

def decrypt(input_text):
    # Decrypt the input text by reversing the shift
    shift = 26 - 10
    code_dict = create_dict(shift)
    result = []
    for letter in input_text:
        result.append(code_dict[letter])
    return ''.join(result)

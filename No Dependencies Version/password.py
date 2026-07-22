import string
import secrets

alphabet = list(string.ascii_letters)
symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]

def number_generator(x):
    return secrets.randbelow(x)

def patch_sequence(a, b):
    index = number_generator(len(alphabet))
    c = alphabet[index]
    seq = f"{b}{a}{c}"
    return seq

def generate_sequence():
    password_set = set()
    password_set.add(alphabet[number_generator(len(alphabet))])
    password_set.add(number_generator(10))
    password_set.update(symbols[number_generator(len(symbols))] for _ in range(2))

    while len(password_set) < 12:
        token = number_generator(2)
        match token:
            case 0:
                index = number_generator(len(alphabet))
                password_set.add(alphabet[index])
            case 1:
                num = number_generator(10)
                password_set.add(num)

    
    sequence = ""
    nested_sequence = []
    for char in password_set:
        sequence += str(char)

        if len(sequence) == 3:
            nested_sequence.append(sequence)
            sequence = ""
    
    final_sequence = ""
    for pad in nested_sequence:
        if (pad == "".join(sorted(pad))):
            new_pad = patch_sequence(pad[0], pad[1])
            final_sequence += new_pad
        else:
            final_sequence += pad
    
    return final_sequence

password = generate_sequence()
print(f"Generated password: {password}")
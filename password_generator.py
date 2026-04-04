import string
import secrets
import re
import pyperclip

alphabet = list(string.ascii_letters)
symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]

def number_generator(x):
    return secrets.randbelow(x)

def find_consecutives(s: str) -> bool:
    return bool(re.search(r'[A-Za-z]{3,}|\d{3,}', s))

def scramble_sequence(string_item):
    seq = list(string_item)
    scrambled_seq = list()

    while len(seq) > 1:
        index = secrets.randbelow(len(seq))
        scrambled_seq.append(seq[index])
        seq.pop(index)
        
    scrambled_seq.append("".join(seq))
    return "".join(scrambled_seq)

def generate_sequence():
    password_list = list()
    password_list.append(secrets.choice(alphabet).upper())                                         #Include at least 1 uppercase letter
    password_list.append(secrets.choice(alphabet).lower())                                         #Include at least 1 lowercase letter
    password_list.append(str(number_generator(10)))                                                #Include at least 1 single digit integer
    password_list.append(secrets.choice(symbols)                                                   #Include 1 symbol                                                        

    while len(password_list) < 12:
        token = number_generator(2)
        match token:
            case 0:
                password_list.append(secrets.choice(alphabet))
            case 1:
                password_list.append(str(number_generator(10)))

    sequence_one = "".join(password_list)
    sequence_two = scramble_sequence(sequence_one)
    
    while find_consecutives(sequence_two):
        sequence_two = scramble_sequence(sequence_one)

    return sequence_two

password = generate_sequence()
pyperclip.copy(password)
print(f"Password copied to clipboard: {password}")

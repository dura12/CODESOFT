import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def no_letter():
    no_char = random.randint(6, 8)
    return no_char

def no_numbers():
    no_num = random.randint(2, 4)
    return no_num

def no_symbols():
    no_symbol = random.randint(2, 4)
    return no_symbol

def generate_password(length):
    password = []
    l = no_letter()
    for i in range(l):
        g = random.choice(letters)
        password.append(g)
    n = no_numbers()
    for i in range(n):
        v = random.choice(numbers)
        password.append(v)
    s = no_symbols()
    for i in range(s):
        m = random.choice(symbols)
        password.append(m)
    random.shuffle(password)
    if len(password) > length:
        password = password[:length]
    elif len(password) < length:
        password += random.choice(letters) * (length - len(password))
    password = "".join(password)
    return password


print("Password Generator")
print("------------------")
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:", password)



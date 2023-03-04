from msilib.schema import Error
import random

def generate_password(length):
    password = []
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    if length >=6 and length <= 32:
        for i in range(length):
            password.append(random.choice(characters))

        password = "".join(password)  
        return password
    else:
        raise TypeError

if __name__ == "__main__":
    generate_password(20)
from string import ascii_letters, ascii_lowercase, whitespace
from itertools import cycle

def encrypt(plaintext, key, mode="encrypt"):
    length = len(ascii_lowercase)
    ciphertext = ""
    key_iterator = cycle(key)
    for letter in plaintext:
        if letter in whitespace:
            ciphertext += " "
            continue
        key_letter = next(key_iterator)
        index = (ascii_letters.index(letter) + ascii_letters.index(key_letter)) % length
        ciphertext += ascii_letters[index]
    
    return ciphertext

def decrypt(ciphertext, key):
    length = len(ascii_lowercase)
    plaintext = ""
    key_iterator = cycle(key)
    for letter in ciphertext:
        if letter in whitespace:
            plaintext += " "
            continue
        key_letter = next(key_iterator)
        index = (ascii_letters.index(letter) - ascii_letters.index(key_letter)) % length
        plaintext += ascii_letters[index]
    
    return plaintext

if __name__ == "__main__":
    plaintext = "This is basic implementation of Vignere Cipher"
    key = "pizza"
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
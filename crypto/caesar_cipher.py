import string

# perform actual cipher operations
def crypto_operations(text: str, sub: int, mode: str="encrypt") -> str:
    ciphertext = ""
    alphabet_len = len(string.ascii_lowercase)

    # select encrypt/decrypt mode
    if mode == "decrypt":
        sub *= -1

    for letter in text:
        # lowercase characters
        if letter in string.ascii_lowercase:
            index = ( string.ascii_lowercase.find(letter) + sub ) % alphabet_len
            ciphertext += string.ascii_lowercase[index]
        # uppercase characters
        elif letter in string.ascii_uppercase:
            index = ( string.ascii_uppercase.find(letter) + sub ) % alphabet_len
            ciphertext += string.ascii_uppercase[index]
        # whitespace and other characters
        else:
            ciphertext += letter

    return ciphertext

def encrypt(text, sub):
    print("encrypt")
    return crypto_operations(text, sub)

def decrypt(text,sub):
    print("decrypt")
    return crypto_operations(text, sub, mode="decrypt")


if __name__ == "__main__":
    while True:
        mode = int(input("Select mode: 1 to encrypt, 2 to decrypt: "))
        test = input("Testing: ")
        substitution_number = int(input("Substitution number: "))
        if mode == 1:
            print(encrypt(test,substitution_number))
        elif mode == 2:
            print(decrypt(test,substitution_number))
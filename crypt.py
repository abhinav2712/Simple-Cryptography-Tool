# Import the necessary modules
import string

# Define the Caesar Cipher encryption function
def caesar_cipher(plain_text, shift):
    # Create a mapping of the alphabet to its shifted position
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    # Encrypt the plain text
    cipher_text = plain_text.translate(table)
    return cipher_text

# Define the Vigenère Cipher encryption function
def vigenere_cipher(plain_text, key):
    # Create a mapping of the alphabet to its shifted position
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_len = len(key)
    shifted_alphabets = [
        alphabet[i:] + alphabet[:i] for i in range(len(alphabet))
    ]

    # Encrypt the plain text
    cipher_text = ""
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shifted_alphabet = shifted_alphabets[ord(key[i % key_len]) - 97]
            table = str.maketrans(alphabet, shifted_alphabet)
            cipher_text += char.translate(table)
        else:
            cipher_text += char
    return cipher_text

# Get the user's input
message = input("Enter the message to encrypt/decrypt: ")
key = input("Enter the key: ")
cipher_type = input("Enter the cipher type (C for Caesar, V for Vigenère): ")

# Encrypt or decrypt the message
if cipher_type.lower() == "c":
    shift = int(input("Enter the shift value: "))
    result = caesar_cipher(message, shift)
elif cipher_type.lower() == "v":
    result = vigenere_cipher(message, key)

# Display the result
print("Result:", result)

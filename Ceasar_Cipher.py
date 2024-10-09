import string

# Caesar Cipher (geser 3)
def caesar_encrypt(message, shift=3):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr(start + (ord(char) - start + shift) % 26)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift=3):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_message += chr(start + (ord(char) - start - shift) % 26)
        else:
            decrypted_message += char
    return decrypted_message

# Contoh penggunaan Caesar Cipher
message = "Hello, World!"
encrypted_message = caesar_encrypt(message)
decrypted_message = caesar_decrypt(encrypted_message)

print(f"Caesar Cipher\nOriginal: {message}\nEncrypted: {encrypted_message}\nDecrypted: {decrypted_message}\n")

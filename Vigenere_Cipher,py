import random
import string

# Fungsi untuk generate key disamakan panjangnya dengan message
def generate_key(message, key=None):
    if key:
        key = list(key)
        if len(message) == len(key):
            return "".join(key)
        else:
            for i in range(len(message) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)
    else:
        # Jika key tidak diberikan, generate key acak
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(len(message)))

# Fungsi enkripsi Vigenère Cipher
def encrypt_message(message, key, explain=False):
    encrypted_message = []
    if explain:
        print("\nProses Enkripsi:")
    for i in range(len(message)):
        shift = (ord(message[i]) + ord(key[i])) % 26
        encrypted_char = chr(shift + 65)  # 65 = 'A' dalam ASCII
        encrypted_message.append(encrypted_char)
        
        # Penjelasan setiap langkah (hanya jika user ingin)
        if explain:
            print(f"Huruf Pesan: {message[i]} ({ord(message[i]) - 65}), Huruf Key: {key[i]} ({ord(key[i]) - 65})")
            print(f"Shift: ({ord(message[i]) - 65} + {ord(key[i]) - 65}) % 26 = {shift}")
            print(f"Huruf Terenkripsi: {encrypted_char}\n")
    
    return "".join(encrypted_message)

# Fungsi dekripsi Vigenère Cipher
def decrypt_message(encrypted_message, key, explain=False):
    decrypted_message = []
    if explain:
        print("\nProses Dekripsi:")
    for i in range(len(encrypted_message)):
        shift = (ord(encrypted_message[i]) - ord(key[i]) + 26) % 26
        decrypted_char = chr(shift + 65)
        decrypted_message.append(decrypted_char)
        
        # Penjelasan setiap langkah (hanya jika user ingin)
        if explain:
            print(f"Huruf Terenkripsi: {encrypted_message[i]} ({ord(encrypted_message[i]) - 65}), Huruf Key: {key[i]} ({ord(key[i]) - 65})")
            print(f"Shift: ({ord(encrypted_message[i]) - 65} - {ord(key[i]) - 65} + 26) % 26 = {shift}")
            print(f"Huruf Asli: {decrypted_char}\n")
    
    return "".join(decrypted_message)

def vigenere_cipher():
    message = input("Masukkan pesan yang ingin dienkripsi: ").upper()

    key = input("Masukkan key (tekan Enter untuk generate key acak): ").upper()

    generated_key = generate_key(message, key if key else None)

    explain_choice = input("Ingin penjelasan detail langkah-langkah enkripsi dan dekripsi? (ya/tidak): ").lower()
    explain = explain_choice == 'ya'
    
    print(f"\nOriginal Message: {message}")
    if key:
        print(f"Key (dari user): {key}")
    else:
        print("Key tidak diberikan, generate key acak...")
    print(f"Generated Key: {generated_key}")

    encrypted_message = encrypt_message(message, generated_key, explain)

    decrypted_message = decrypt_message(encrypted_message, generated_key, explain)

    print(f"\nHasil Akhir:")
    print(f"Pesan Asli: {message}")
    print(f"Pesan Terenkripsi: {encrypted_message}")
    print(f"Pesan Didekripsi Kembali: {decrypted_message}")

vigenere_cipher()
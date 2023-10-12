def vigenere_cipher(text, key, decrypt=False):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            if decrypt:
                shift = -shift
            if char.isupper():
                result.append(chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def login(username, password, stored_username, stored_password):
    # Enkripsi password yang dimasukkan dengan kunci (contoh: "SECRET")
    encrypted_password = vigenere_cipher(password, "SECRET")

    # Verifikasi username dan password
    if username == stored_username and encrypted_password == stored_password:
        return True
    else:
        return False

# Contoh penggunaan
stored_username = "Mahfud123"
stored_password = vigenere_cipher("password123", "SECRET")

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if login(username, password, stored_username, stored_password):
    print("Login berhasil!")
else:
    print("Login gagal.")

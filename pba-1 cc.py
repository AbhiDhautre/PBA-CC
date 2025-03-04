def format_input(text):
    
    return ''.join(filter(str.isalpha, text)).upper()

def vigenere_encrypt(plaintext, key):
    
    plaintext = format_input(plaintext)  
    key = format_input(key)  
    ciphertext = ""
    
    key_index = 0
    key_length = len(key)

    for letter in plaintext:
        shift = ord(key[key_index]) - ord('A')  
        encrypted_letter = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        ciphertext += encrypted_letter
        key_index = (key_index + 1) % key_length 
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    
    key = format_input(key)  
    plaintext = ""
    
    key_index = 0
    key_length = len(key)

    for letter in ciphertext:
        shift = ord(key[key_index]) - ord('A')  
        decrypted_letter = chr((ord(letter) - ord('A') - shift + 26) % 26 + ord('A'))
        plaintext += decrypted_letter
        key_index = (key_index + 1) % key_length  

    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")


ciphertext = vigenere_encrypt(plaintext, key)
print("\nEncrypted Text:", ciphertext)


decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)

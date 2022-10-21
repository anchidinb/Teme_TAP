from cryptography.fernet import Fernet

message = input("Introduceti textul pe care vreti sa il criptati: ")
key = Fernet.generate_key()
fernet = Fernet(key)
encrypted_text = fernet.encrypt(message.encode())
decrypted_text = fernet.decrypt(encrypted_text).decode()
print('Textul necriptat: ', message)
print('Textul criptat: ', encrypted_text)
print('Textul decriptat: ', decrypted_text)

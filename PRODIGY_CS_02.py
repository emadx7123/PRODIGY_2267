from cryptography.fernet import Fernet
git
key = Fernet.generate_key()
print(key)
fernet = Fernet(key)
#Writing
with open('key.key', 'wb') as filekey:
    filekey.write(key)
#reading
with open('key.key', 'rb') as filekey:
    key = filekey.read()
#read the file
with open('LOGO-27.jpg', 'rb') as file:
    orignal_file = file.read()
encrypted = fernet.encrypt(orignal_file)
with open('enc LOGO-27.jpg', 'wb') as file:
    file.write(encrypted)
# Decryting the Audio
fernet = Fernet(key)
with open('enc LOGO-27.jpg', 'rb') as file:
    encrypted_file = file.read()
decrypted = fernet.decrypt(encrypted_file)
with open('dec LOGO-27.jpg', 'wb') as file:
    file.write(decrypted)
 
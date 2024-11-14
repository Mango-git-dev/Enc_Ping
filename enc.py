# tạo file 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# đọc nội dung của file cần enc
with open('script.py', 'rb') as file: # thay script.py thành file muốn enc
    file_data = file.read()

key = os.urandom(32)
iv = os.urandom(16)  

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
encrypted_data = encryptor.update(file_data) + encryptor.finalize()

encoded_key = base64.b64encode(key).decode('utf-8')
encoded_iv = base64.b64encode(iv).decode('utf-8')
encoded_encrypted_data = base64.b64encode(encrypted_data).decode('utf-8')

# tạo file .py(thay output.py ở dưới thành file đầu ra)
with open('output.py', 'w', encoding='utf-8') as encrypted_file:  
    encrypted_file.write(f"""
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

encoded_key = '{encoded_key}'
encoded_iv = '{encoded_iv}'
encoded_encrypted_data = '{encoded_encrypted_data}'

key = base64.b64decode(encoded_key)
iv = base64.b64decode(encoded_iv)
encrypted_data = base64.b64decode(encoded_encrypted_data)

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

exec(decrypted_data.decode('utf-8'))
    """)

print("File output.py đã được mã hóa.") # ở đây cũng thay output.py thành file đầu ra mà người dùng muốn

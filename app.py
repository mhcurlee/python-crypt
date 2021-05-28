
from cryptography.fernet import Fernet
import os


# encryption key from env var
if os.environ.get('SEC_KEY'): 
  key = os.environ.get('SEC_KEY')  
else:
  print("SEC_KEY env var not found")
  sys.exit(1)


def encrypt_data(data):
  """Returns encyrpted string"""
  fernet = Fernet(key) 
  return fernet.encrypt(data.encode()).decode('UTF-8')


def decrypt_data(data):
  """Returns decyrpted string"""
  fernet = Fernet(key) 
  byte_data = bytes(data, 'UTF-8')
  return fernet.decrypt(byte_data).decode()
  


with open('README.md', 'r') as file:
   secret_data = encrypt_data(file.read())



with open('secret.txt', 'w') as file:
  file.write(secret_data)



with open('secret.txt', 'r') as file:
  file_data = file.read()
  

print(decrypt_data(file_data))




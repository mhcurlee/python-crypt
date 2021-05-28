#!/usr/bin/env python


from cryptography.fernet import Fernet
import os
import sys

# first arg is file name
file_name = sys.argv[1]

# encryption key from env var
if os.environ.get('SEC_KEY'): 
  key = os.environ.get('SEC_KEY')  
else:
  print("SEC_KEY env var not found")
  sys.exit(1)



def decrypt_data(data):
  """Returns decyrpted string"""
  try:
    fernet = Fernet(key) 
    byte_data = bytes(data, 'UTF-8')
    return fernet.decrypt(byte_data).decode()

  except Exception as err:
    print(err)
    sys.exit(1)
  

# Load file in command arg
try:
  with open(file_name, 'r') as file:
    file_data = file.read()
except Exception as err:
    print(err)
    sys.exit(1)



# decrypt data
print(decrypt_data(file_data))




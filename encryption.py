from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad,unpad
import argparse

#! Getting inputs in command-line
parser = argparse.ArgumentParser(description="Encrypt a file")
parser.add_argument('filename', help='File to encrypt')
parser.add_argument('-p', '--password', help='Password')
args = parser.parse_args()
file_name = args.filename
pwd = args.password


def password(pwd):    
    ''' Password hashing to 16 bytes '''
    hashed_pwd = SHA256.new(pwd.encode("utf-8")).digest()
    return hashed_pwd


def encoding(file_name,hashed_pwd):
    ''' Data encoding '''
    try :
        with open(file_name,'rb') as entry:
            data = entry.read()
            encrypt = AES.new(hashed_pwd,AES.MODE_CBC)
            message = encrypt.encrypt(pad(data,AES.block_size))
        with open(file_name,'wb') as wfile:
            wfile.write(encrypt.iv)
            wfile.write(message)
    except FileNotFoundError :
        print("Error : File Not Found")        

#! Getting input while running the python file
# file_name = input("Enter the file name with extension : ")
# pwd = input("Enter your password : ")

encoding(file_name,password(pwd))
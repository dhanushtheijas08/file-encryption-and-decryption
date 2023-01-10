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

def decoding(file_name,hashed_pwd):
    ''' Data decoding '''
    try:
        with open(file_name,'rb') as ofile:
          odata_iv = ofile.read(16)
          odata = ofile.read()
          decrypt = AES.new(hashed_pwd,AES.MODE_CBC,iv=odata_iv)
        with open(file_name,'wb') as lfile:
          message = unpad(decrypt.decrypt(odata),AES.block_size)
          lfile.write(message)
    except FileNotFoundError : 
        print("Error : File Not Found") 
    except ValueError:
        print("Error : Incorrect Password")     
            
#! Getting input while running the python file
# file_name = input("Enter the file name to be decrypted with extension : ")
# pwd = input("Enter your password : ")
decoding(file_name,password(pwd))
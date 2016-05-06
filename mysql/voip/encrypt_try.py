#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os

def AESEncryption(data):
        def pad(s):
                return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

        def encrypt(message, key, key_size=256):   
                #print "hhhhhhhhhhiiiiiiiii"
                message = pad(message)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return iv + cipher.encrypt(message)

        """def encrypt_file(file_name, key):
                with open(filename, 'rb') as fo:
                        plaintext = fo.read()
                enc = encrypt(plaintext, key)
                with open('encrypted files/'+file_name+'.enc', 'wb') as fo:
                        fo.write(enc)"""

        """def decrypt_file(file_name, key):
                with open(file_name, 'rb') as fo:
                        ciphertext = fo.read()
                dec = decrypt(ciphertext, key)
                with open('dec_'+file_name[:-4], 'wb') as fo:
                        fo.write(dec)"""


        key ='0123456789abcdef'
        #directory,file_name=os.path.split(filename)      
        enc=encrypt(data, key)
        #print enc
        #decrypt_file('a.rar.enc', key)
        #return file_name+".enc"
        return enc



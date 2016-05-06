#!/usr/bin/python3

from Crypto import Random          # random numbers generated from crpto  library 
from Crypto.Cipher import AES      # use AES algo
import os                         

def AESDecryption(ciphertext):        # function for decryption
	def pad(s):      # make each block size of 16 bit
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def decrypt(ciphertext, key):      #    take ciphertext and key as a input parameter
		iv = ciphertext[:AES.block_size]    #  
		cipher = AES.new(key, AES.MODE_CBC, iv)    #  
		plaintext = cipher.decrypt(ciphertext[AES.block_size:])  # changes it to plain text
		return plaintext.rstrip(b"\0")   # return that plain text


	key ='0123456789abcdef'     # decrpytion key 
	dec = decrypt(ciphertext, key)   # in dec data stored
	#print dec
    #directory,file_name=os.path.split(filename)
	#encrypt_file(file_name, key)
	#decrypt_file(file_name, key)
    #return file_name+".enc"
	return dec    # dec returns original data

#!/usr/bin/python3
import argparse
from Crypto.Cipher import AES
from Crypto import Random

def encrypt_with_aes(text, key, mode):
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key,mode, iv)
	return iv + cipher.encrypt(text)

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("file")
	parser.add_argument("key", help="16 byte key")

	args = parser.parse_args()
	filename=args.file
	filename_out = filename[:-2] + "out"	

	key =str.encode(args.key)
	mode = AES.MODE_CBC
	print(len(key))
	with open(filename, 'rb') as f_in, open(filename_out,'wb') as f_out:
		text = f_in.read(16)
		f_out.write(encrypt_with_aes(text, key, mode))


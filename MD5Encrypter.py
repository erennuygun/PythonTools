#---------------------------#
# Base64Encode by Sainteryn #
#---------------------------#
#############################
#---------------------------#

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5

def encrypt():

	data = raw_input("Please enter the text to be hash : ")
	hash=md5.new(data)
	print("Hash : %s " % (hash.hexdigest()))

def main ():
	print("\n\n")
	print("#---------------------------#")
	print("#-MD5Encrypter by Sainteryn-#")
	print("#---------------------------#")
	print ("#-- https://cyseclab.com --#")
	print("#---------------------------#")
	print("\n\n")
	encrypt()
main()

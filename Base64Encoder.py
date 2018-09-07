#---------------------------#
# Base64Encode by Sainteryn #
#---------------------------#
#############################
#---------------------------#

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encrypt():

	data = raw_input("Please enter the data to be encrypt : ")
	hash = data.encode('base64','strict')
	print(hash)

def main():

	print("\n\n")
	print("#---------------------------#")
	print("#-Base64Encoder by Sainteryn-#")
	print("#---------------------------#")
	print ("#-- https://cyseclab.com --#")
	print("#---------------------------#")
	print("\n\n")
	encrypt()
main()


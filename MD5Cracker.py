#---------------------------#
# Base64Encode by Sainteryn #
#---------------------------#
#############################
#---------------------------#

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5



def crack():
	counter = 1
	hash = raw_input("Please enter the MD5 Hash to be decrypt : ")
	wordlist = raw_input("Please enter the wordlist file path : ")

	try:
		wordlist = open(wordlist, "r")
	except:
		print ( "\nFile not found ")
		quit()

	for password in wordlist:

		filemd5 = md5.new(password.strip()).hexdigest()
 		print("Trying password %d: %s " % (counter,password.strip()))

		counter += 1

		if hash == filemd5:
			print ("\nPassword Found.  \nPassword is : %s" % (password))
			break

		else:
			print("\nPassword not Found. ")


def main():
	crack()
print("\n\n")
print("#---------------------------#")
print("#-MD5Cracker by Sainteryn-#")
print("#---------------------------#")
print ("#-- https://cyseclab.com --#")
print("#---------------------------#")
print("\n\n")

main()

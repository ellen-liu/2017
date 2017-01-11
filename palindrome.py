'''
January 6, 2017

Program to check if the given string is a palindrome or not.
'''

word = raw_input("Enter a string: ")
def palindrome(word):
	if word == word[::-1]:
		print "%s is a palindrome :)" % word
	else:
		print "%s is not a palindrome :(" % word

palindrome(word)

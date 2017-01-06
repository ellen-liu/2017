# Program to count the number of vowels in a string and report a sum of each vowel found

def count_vowels():
	word = raw_input("Enter a word: ")
	upper = list(word.upper())
	vowels = {"A":0, "E": 0, "I": 0, "O": 0, "U": 0}
	for i in xrange(0,len(word)):
		if upper[i] in vowels.keys():
			vowels[upper[i]] += 1
	num = sum(vowels.values())
	print "There are %d vowels in the string %s" % (num, word)
	print " A: %d \n E: %d \n I: %d \n O: %d \n U: %d" % (vowels.get("A"), vowels.get("E"), vowels.get("I"), vowels.get("O"), vowels.get("U"))

count_vowels()
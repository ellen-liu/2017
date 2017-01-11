# Program to take in user birth date and display horoscope, scraped from a website

def show_sign():
	print "(Don't enter any leading zeroes)"
	month = raw_input("What month were you born in? (ex. if January, input 1): ")
	day = raw_input("What date? (ex. 31): ")

	sign = get_sign(month,day)
	print sign
	print "Your sign is %s" % sign

def get_sign(month,date):
	if ((month == 1 and date >= 20) or (month == 2 and date <= 18)):
		return "Aquarius"
	elif ((month == 2 and date >= 19) or (month == 3 and date <= 20)):
		return "Pisces"
	elif ((month == 3 and date >= 21) or (month == 4 and date <= 19)):
		return "Aries"
	elif ((month == 4 and date >= 20) or (month == 5 and date <= 20)):
		return "Taurus"
	elif ((month == 5 and date >= 21) or (month == 6 and date <= 20)):
		return "Gemini"
	elif ((month == 6 and date >= 21) or (month == 7 and date <= 22)):
		return "Cancer"
	elif ((month == 7 and date >= 23) or (month == 8 and date <= 22)):
		return "Leo"
	elif ((month == 8 and date >= 23) or (month == 9 and date <= 22)):
		return "Virgo"
	elif ((month == 9 and date >= 23) or (month == 10 and date <= 22)):
		return "Libra"
	elif ((month == 10 and date >= 23) or (month == 11 and date <= 21)):
		return "Scorpio"
	elif ((month == 11 and date >= 22) or (month == 12 and date <= 21)):
		return "Sagittarius"
	elif ((month == 12 and date >= 22) or (month == 1 and date <= 19)):
		return "Capricorn"

show_sign()
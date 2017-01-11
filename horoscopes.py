'''
January 10, 2017

Program to take in user birth date and display horoscope, 
scraped from pages on an astrology website. Used tutorial for scraping 
a web page using BeautifulSoup on AnalyticsVidhya
'''

# import library used to query a website
import urllib2
# import BeautifulSoup functions to parse the data from the web
from bs4 import BeautifulSoup

def main():
	sign = show_sign()
	find_horoscope(sign)

def show_sign():
	print "\nTODAY'S HOROSCOPES"
	print "\n(Don't enter any leading zeroes)"
	month = int(raw_input("What month were you born in? (ex. if January, input 1): "))
	day = int(raw_input("What date? (ex. 31): "))

	sign = get_sign(month,day)
	return sign

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

def find_horoscope(sign):

	# Assign horoscope site
	base = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
	if sign == "Aries":
		scrape = base + "1"
	elif sign == "Taurus":
		scrape = base + "2"
	elif sign == "Gemini":
		scrape = base + "3"
	elif sign == "Cancer":
		scrape = base + "4"
	elif sign == "Leo":
		scrape = base + "5"
	elif sign == "Virgo":
		scrape = base + "6"
	elif sign == "Libra":
		scrape = base + "7"
	elif sign == "Scorpio":
		scrape = base + "8"
	elif sign == "Sagittarius":
		scrape = base + "9"
	elif sign == "Capricorn":
		scrape = base + "10"
	elif sign == "Aquarius":
		scrape = base + "11"
	elif sign == "Pisces":
		scrape = base + "12"

	# Query website and return html to the variable 'page'
	page = urllib2.urlopen(scrape)

	# Parse html in the 'page variable' and store it in BeautifulSoup format
	soup = BeautifulSoup(page, "html.parser")
	horoscope = str(soup.find(class_ = "block-horoscope-text f16 l20"))
	date = str(soup.find(class_ = "block-horoscope-date"))

	print "\n- - - - - %s - - - - -" % (sign.upper())
	print "%s\n" % remove_html(date)
	print remove_html(horoscope)
	print "\n"

def remove_html(horoscope):
	# http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
	tag = False
	quote = False
	out = ""

	for c in horoscope:
		if c == '<' and not quote:
			tag = True
		elif c == '>' and not quote:
			tag = False
		elif (c == '"' or c == "'") and tag:
			quote = not quote
		elif not tag:
			out = out + c
	return out.strip()
main()








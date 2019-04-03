import requests
import re
from bs4 import BeautifulSoup
#import decorator
import classPerson
import dbC2
from classPerson import person

def check(function) :
	def wrapper(*args,**kwargs) :
		if dbC2.isInDb(*args,**kwargs):
			return function(*args,**kwargs)
	return wrapper

@check
def scrape(username) :
	if username in person.usedNames.keys() :
		return person.usedNames[username].show()
	else: 	
		userObj = person(username)
		url = f'https://en-gb.facebook.com/{username}'
		temp = requests.get(url)
		soup = BeautifulSoup(temp.content, 'html5lib')

		#Display Name 
		name = soup.find('a', {'class' : '_2nlw _2nlv'})
		print(f"Display name : {name.get_text()}")
 
		
		#work
		work = []
		#temp = soup.find('ul',{'class' : 'uiList fbProfileEditExperiences _4kg _4ks'}) 
		for temp in soup.find('ul',{'class' : 'uiList fbProfileEditExperiences _4kg _4ks'}) :
			#print(temp.get_text(), sep="\n")
			work.append(temp.get_text())
		if work != [] :
			userObj.work = work
			print("\nWork : ")
			print(*work, sep='\n')
		
		#city
		city = soup.find('span',{'class' : '_2iel _50f7'});
		userObj.city = city.get_text().strip()
		print(f"\nCurrent City : {userObj.city}")

		#favorites
		fav = []
		favorites = soup.find('div', {'class':'uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData'})
		if favorites is not None :
			for temp in soup.findAll('div', {'class':'uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData'}):
				fav.append(temp.get_text())
			print("\nFavorites : ")
			print(*fav, sep='\n')        
		else :
			print("No favorites")

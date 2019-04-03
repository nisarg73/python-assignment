import dbC2

class person :
	usedNames = {} 
	#constructor
	def __init__(self,name,**kwargs) :
		if name not in person.usedNames.keys() :
			self.name = name
			person.usedNames[name] = self
		else :
			flag = False #for unittest
			#raise Exception("name already used once")
		if 'work' in kwargs.keys() :
			self.work = kwargs['work']
		if 'city' in kwargs.keys() :
			self.city = kwargs['city']
		else :
			self.city = 'Roorkee'


	def show(self) :
		print(f'My name is {self.name} and my current city is {self.city}')

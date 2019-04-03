import unittest
from classPerson2 import person
from scrape2 import scrape
from dbC2 import isInDb
class test(unittest.TestCase) :
	def test(self) :
		self.assertTrue(True)

	#for dbC2.py
	def test_in_db(self) :
		temp = 'ayushjainaj20'
		self.assertTrue(isInDb(temp))
	def test_not_in_db(self) :
		temp = 'randomUser'
		self.assertFalse(isInDb(temp))
	
	#for classPerson2.py
	"""
	def test_object_name_taken(self) :
		temp = person('alpha')
		temp2 = person('alpha')
		self.assertEqual(temp2,False)
	"""
	def test_city_present(self) :
		temp = person('shaddygarg')
		self.assertEqual(temp.city,'Roorkee')
	def test_no_city(self) :
		temp = person('random')
		self.assertEqual(temp.city,'Roorkee')
	def test_show_function(self) :
		temp = scrape('shaddygarg')
		temp2 = scrape('shaddygarg')
		self.assertEqual(temp2,"Show function")

if __name__ =='__main__':
    unittest.main()
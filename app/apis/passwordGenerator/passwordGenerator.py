import string
import random

class passgen:
	def __init__(self, passlength, capitalLetter, lowCaseLetter, specialCharacters):
		self.__passlength = passlength # Private __  # Protected _
		self.__capitalLetter = capitalLetter
		self.__lowCaseLetter = lowCaseLetter
		self.__specialCharacters = specialCharacters

	def get_passlength(self):
		return self.__passlength

	def get_capitalLetter(self):
		return self.__capitalLetter

	def get_lowCaseLetter(self):
		return self.__lowCaseLetter

	def get_specialCharacters(self):
		return self.__specialCharacters

	def get_asciiList(self):
		delete = ['\t','\x0c','\x0b','\n','\r']
		asciis = [x for x in string.printable if delete.__contains__(x) == False]
		return asciis

	def cleanCapitalLetters(self, lista):
		capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		cleanList = [x for x in lista if capitalLetters.__contains__(x) == False]
		return cleanList

	def cleanLowerCaseLetters(self, lista):
		lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		cleanList = [x for x in lista if lowerCaseLetters.__contains__(x) == False]
		return cleanList

	def cleanSpecialCharacters(self,lista):
		specialCharacters = ['#', '$', '%', '&', '(', ')', '*', '+', '/', '<', '=', '>', '@', '[', 
		'\\', ']', '{', '|', '}','!', '"' , "'" ,',' , '-' , '.' , ':', ';' , '?' , '^' , '_' , '`' , '~']
		cleanList = [x for x in lista if specialCharacters.__contains__(x) == False]
		return cleanList

	def joinListValues(self,lista):
		join = ''
		for x in lista:
			join += str(x)
		return join

	def generatePass(self):
		if passgen.get_passlength(self) < 30:
			password = list()
			asciis = passgen.get_asciiList(self)	

			if passgen.get_capitalLetter(self) == False:
				asciis = passgen.cleanCapitalLetters(self,asciis)
			if passgen.get_lowCaseLetter(self) == False:
				asciis = passgen.cleanLowerCaseLetters(self,asciis)
			if passgen.get_specialCharacters(self) == False:
				asciis = passgen.cleanSpecialCharacters(self,asciis)
			while len(asciis) <= passgen.get_passlength(self):
				asciis.extend(asciis)
			for word in range(passgen.get_passlength(self)):
				randomNumb = random.randint(0,len(asciis)-1)
				password.append(asciis[randomNumb])
			return passgen.joinListValues(self,password)
		else:
			return 'You have overpassed the maximum length, the maximum length is 29 characters'
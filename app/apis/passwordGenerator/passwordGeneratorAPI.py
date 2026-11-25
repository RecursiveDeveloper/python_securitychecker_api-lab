from flask_restful import Resource
from apis.passwordGenerator.passwordGenerator import passgen

class passwordGeneratorAPI(Resource):
	def get(self, passlength, capitalLetter, lowCaseLetter, specialCharacters):
		verify = [0,1]
		try:
			if verify.__contains__(capitalLetter) and verify.__contains__(lowCaseLetter) and verify.__contains__(specialCharacters):
				passwordClass = passgen(passlength, capitalLetter, lowCaseLetter, specialCharacters)
				try:
					passString = passwordClass.generatePass()
					return { 'password' : passString }
				except Exception as e:
					print('An error has occurred during the password generating process, please verify your params data type or conexion.\nError info: {}'.format(e))
			else:
				raise Exception('An error has occurred, please verify your params data type, they must be int type, 0 or 1 . Otherwise, an error is raised')
		except Exception as e:
			print('An error has occurred, please verify your params data type or conexion.\nError info: {}'.format(e))
			return {'GeneratedPassword' : 'Error'}
from app import app
import unittest
import json

class FlaskTestCace(unittest.TestCase):
	# Ensure that flask was set up correctly
	def test_flask(self):
		tester=app.test_client(self)
		response=tester.get('/',content_type='html/text')
		self.assertEqual(response.status_code,200)

	# Ensure that the index page loads correctly
	def test_index(self):
		tester=app.test_client(self)
		response=tester.get('/',content_type='html/text')
		self.assertTrue('Caesar cipher' in response.data)

	# test encrypt
	def test_encrypt(self):
		tester=app.test_client(self)
		response = tester.get('/crypt',
			data=json.dumps({"crypt":"like the water","step":"2"}),
			follow_redirects=True)
		print response.data
		self.assertTrue('gsdfgs' in response.data)

if __name__=='__main__':
	unittest.main()

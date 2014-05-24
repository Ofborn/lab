from person.views import PersonList
from person.views import PersonDestroy
from rest_framework import status
from django.test import Client
import nose.tools as tdd

class TestPerson (object):
	def setup (self):
		self.PersonList = PersonList()
		self.PersonDestroy = PersonDestroy()
		self.Client = Client()
		self.facebookId1 = 100001891465941
		self.facebookId2 = 100001891465940
		self.Client.post('/person/', {'facebookId' : self.facebookId1})

	def test_getFacebookData (self):
		data = {u'username': u'Soulight.Events', u'first_name': u'SoulightEvents', u'last_name': u'Grp', u'name': u'SoulightEvents Grp', u'locale': u'en_US', u'gender': u'male', u'link': u'https://www.facebook.com/Soulight.Events', 'facebookid': u'100001891465941', u'id': u'100001891465941'}
		response = self.PersonList.getFacebookData(self.facebookId1)
		tdd.assert_equal(response, data)

	def test_get (self):
		data = [{'facebookid': u'100001891465941', 'username': u'Soulight.Events', 'name': u'SoulightEvents Grp', 'gender': u'male'}]
		response = self.Client.get('/person/')
		tdd.assert_equal(response.data , data)

	def test_post (self):
		data = {'facebookid': u'100001891465940', 'username': u'rafael.valverdemartins', 'name': u'Rafael Valverde Martins', 'gender': u'male'}
		response = self.Client.post('/person/', {'facebookId' : self.facebookId2})
		tdd.assert_equal(response.data, data)
		tdd.assert_equal(response.status_code, status.HTTP_201_CREATED)

	def test_get_limit (self):
		data = [{'facebookid': u'100001891465941', 'username': u'Soulight.Events', 'name': u'SoulightEvents Grp', 'gender': u'male'}]
		response = self.Client.get('/person/', {'limit' : '1'})
		tdd.assert_equal(response.data , data)

	def test_get_object (self):
		test_result = self.PersonDestroy.get_object(self.facebookId1)
		tdd.assert_true(test_result)
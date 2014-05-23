from person.models import Person
from person.serializers import PersonSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PersonList (APIView):
	def get (self, request, format = None):
		limit = request.GET.get('limit', None)
		if limit == None:
			person = Person.objects.all()
		else:
			person = Person.objects.all()[:limit]
		serializer = PersonSerializer(person, many = True)
		return Response(serializer.data)

	def post (self, request, format = None):
		facebookId = request.POST.get('facebookId', None)
		data = self.getFacebookData(facebookId)
		serializer = PersonSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def getFacebookData (self, pk):
		import requests
		param = {'id': pk}
		data = requests.get('http://graph.facebook.com/', params = param)
		formatted = data.json()
		if data.status_code == 200:
			formatted['facebookid'] = formatted['id']
		return formatted


class PersonDestroy (APIView):
	def get_object (self, pk):
		try:
			return Person.objects.get(pk = pk)
		except Person.DoesNotExist:
			raise Http404

	def delete (self, request, pk, format = None):
		person = self.get_object(pk)
		person.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
from django.http import JsonResponse
from django.views import View
from .models import Movie

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


class Movies(View):
	def get(self, request):
		if(request.user.is_authenticated):
			user = User.objects.get(id=request.user.id)
			movie_list = list(user.movies.all().values())
			print(movie_list);
			return JsonResponse({
				'Content-Type': 'application/json',
            	'status': 200,
            	'data': movie_list
			}, safe=False)
# Error catching
		else: 
			return JsonResponse({
				'Content-Type': 'application/json',
            	'status': 200,
            	'message': 'Must be logged in to see the data'
				}, safe=False)
# Post route
	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			new_movie = Movie(title=data['title'], description=data['description'])
			new_movie.created_by = request.user
			new_movie.save()
			data['id'] = new_movie.id
			return JsonResponse({'data': data}, safe=False)
		except:
			return JsonResponse({'error': 'not valid data'}, safe=False)
class Movie_detail(View):
	def get(self, request, id):
		movie_list = list(Movies.objects.filter(id=id).values())
		print(movie_list, 'movie_list in movie detail, CHECKED')
		return JsonResponse({'data': movie_list}, safe=False)
	def put(self, request, id):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try: 
			edit_movie = Movie.objects.get(id=id)
			print(edit_movie, 'edit_movie in put route movie detail')
			data_key = list(data.keys())
			print(data_key, 'data_key in put movie detail')
			for key in data_key:
				if key == 'title':
					edit_movie.title = data[key]
				if key == 'description':
					edit_movie.description = data[key]
			edit_movie.created_by = request.user
			edit_movie.save()
			print(edit_movie, 'after the try/for in put route')
			data['id'] = edit_movie.id
			return JsonResponse({'data': data}, safe=False)
		except Movie.DoesNotExist: 
			return JsonResponse({'error': 'Something went wrong'}, safe=False)
	def delete(self, request, id):
		try:
			movie_to_delete = Movie.objects.get(id=id)
			movie_to_delete.delete()
			return JsonResponse({'data': True}, safe=False)
		except: 
			return JsonResponse({'error': 'Something went WRong'}, safe=False)



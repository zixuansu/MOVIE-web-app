import datetime

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session, request

import movie.adapters.repository as repo
import movie.detail.services as services


# Configure Blueprint.
detail_blueprint = Blueprint('detail_bp', __name__,url_prefix='/detail')

@detail_blueprint.route('/movie/<string:title>/',methods=['GET','POST'])
def show_movie(title):
	user = session.get('user_info')
	if not user:
		user = 'tourist'
	if request.method == 'POST':
		moviename = request.form.get('movie')
		username = request.form.get('user')
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%m')
		text = request.form.get('comment')
		comment = {'name':moviename,'user':username,'timestamp':timestamp,'text':text}
		if text != '':
			services.add_comment_to_movie(comment,repo.repo_instance)
			# with open('./datafiles/MovieComment.csv','a+', encoding='utf-8',newline='') as csvfile:    
				# writer=csv.writer(csvfile)
				# writer.writerow([moviename,username,timestamp,text])
	movies = services.get_all_movies(repo.repo_instance)
	movie = services.select_movie(title,repo.repo_instance)
	comments = services.load_movie_comment(movie.title,repo.repo_instance)
	return render_template('/detail/movie.html',movie=movie,user=user,comments=comments)

@detail_blueprint.route('/director/<string:name>/',methods=['GET','POST'])
def show_director(name):
	user = session.get('user_info')
	if not user:
		user = 'tourist'
	if request.method == 'POST':
		directorname = request.form.get('director')
		username = request.form.get('user')
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%m')
		text = request.form.get('comment')
		comment = {'name':directorname,'user':username,'timestamp':timestamp,'text':text}
		if text != '':
			services.add_comment_to_director(comment,repo.repo_instance)
			# with open('./datafiles/DirectorComment.csv','a+', encoding='utf-8',newline='') as csvfile:    
			# 	writer=csv.writer(csvfile)
			# 	writer.writerow([directorname,username,timestamp,text])
	# directors = moviereader.dataset_of_directors
	# director = select_director(directors,name)
	comments = services.load_director_comment(name,repo.repo_instance)
	return render_template('/detail/director.html',director=name,user=user,comments=comments)

@detail_blueprint.route('/actor/<string:name>/',methods=['GET','POST'])
def show_actor(name):
	user = session.get('user_info')
	if not user:
		user = 'tourist'
	if request.method == 'POST':
		actorname = request.form.get('actor')
		username = request.form.get('user')
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%m')
		text = request.form.get('comment')
		comment = {'name':actorname,'user':username,'timestamp':timestamp,'text':text}
		if text != '':
			services.add_comment_to_actor(comment,repo.repo_instance)
			# with open('./datafiles/ActorComment.csv','a+', encoding='utf-8',newline='') as csvfile:    
			# 	writer=csv.writer(csvfile)
			# 	writer.writerow([actorname,username,timestamp,text])
	# actors = moviereader.dataset_of_actors
	# actor = select_actor(actors,name)
	comments = services.load_actor_comment(name,repo.repo_instance)
	return render_template('/detail/actor.html',actor=name,user=user,comments=comments)

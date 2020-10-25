from flask import Blueprint, render_template, redirect, url_for, session, request

import movie.authentication.services as services
import movie.adapters.repository as repo

# Configure Blueprint.
authentication_blueprint = Blueprint(
    'authentication_bp', __name__, url_prefix='/authentication')


@authentication_blueprint.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('./authentication/login.html')
	user = request.form.get('user')
	pwd = request.form.get('pwd')
	messages = services.authenticate_user(user,pwd,repo.repo_instance)
	if messages['state']:
		session['user_info'] = user
		return redirect('/movieslist/')
	else:
		return render_template('./authentication/login.html',message=messages['error'])

@authentication_blueprint.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('./authentication/register.html')
	user = request.form.get('user')
	pwd = request.form.get('pwd')
	messages = services.user_register(user,pwd,repo.repo_instance)
	if messages['state']:
		session['user_info'] = user
		return redirect('/movieslist/')
	else:
		return render_template('./authentication/register.html',message=messages['error'])

@authentication_blueprint.route('/logout')
def logout():
	del session['user_info']
	return redirect('/movieslist/')


from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.forms import RegistrationForm, LoginForm
from application.user.models import User
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=['GET', 'POST'])
def signup_page():
	if current_user.is_authenticated:
		return redirect(url_for('home.home_page'))
	form = RegistrationForm()
	if form.validate_on_submit():
		if User.query.filter_by(email=form.email.data).first():
			flash('Профиль с данной почтой уже существует!', 'danger')
		else:
			hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=hashed_password, profile_picture="default.png", permissions="read+write")
			db.session.add(user)
			db.session.commit()
			flash('Профиль создан, вы можете авторизоваться', 'success')
			return redirect(url_for('auth.login_page'))
	return render_template('signup.html', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login_page():
	if current_user.is_authenticated:
		return redirect(url_for('home.home_page'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('Авторизация успешна!', 'success')
			return redirect(url_for('home.home_page'))
		else:
			flash('Авторизация провальна - проверьте корретность введенных данных', 'danger')
	return render_template('login.html', form=form)


@auth.route("/logout")
@login_required
def logout_page():
	logout_user()
	flash('Вы успешно вышли', 'success')
	return redirect(url_for('home.home_page'))
	

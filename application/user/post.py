from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.forms import RegistrationForm, PostForm
from application.user.models import Post
from application import app, db 
from flask_login import current_user, login_required
from datetime import date

post = Blueprint('post', __name__)


@post.route("/post", methods=["GET", "POST"])
@login_required
def create_post_page():
	if not 'write' in current_user.permissions.split('+'):
		flash("You have no access!", 'danger')
		return redirect(url_for('home.home_page'))

	flash('Придерживайтесь стандарта заполнения', 'success')
	form = PostForm()

	if form.validate_on_submit():
		post = Post(title=form.title.data, topic=form.topic.data, body=form.body.data, author_id=current_user.id, author_name=current_user.name, author_surname=current_user.surname, private=form.private.data, publication_date=date.today(), latest_editing_date=date.today())
		db.session.add(post)
		db.session.commit()
		flash('Ваша публикация создана!', 'success')
		return redirect(url_for('home.home_page'))
	return render_template('post.html', form=form)


@post.route("/edit_<id_>", methods=["GET", "POST"])
@login_required
def edit_post_page(id_):
	if not ('write' in current_user.permissions.split('+') and Post.query.get(int(id_)) and Post.query.get(int(id_)).author_id == current_user.id):
		flash("Недостаточно прав или публикации не существует!", 'danger')
		return redirect(url_for('home.home_page'))
	
	flash('Придерживайтесь стандарта заполнения', 'success')
	form = PostForm()
	if not form.title.data:
		form.make(Post.query.get(int(id_)))

	if form.validate_on_submit():
		post = Post.query.get(int(id_))
		post.title = form.title.data
		post.topic = form.topic.data
		post.body = form.body.data
		post.private = form.private.data
		post.latest_editing_date = date.today()
		db.session.commit()
		flash('Ваша публикация обновлена!', 'success')
		return redirect(url_for('home.home_page'))
	return render_template('post.html', form=form)

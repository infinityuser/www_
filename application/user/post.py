from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.forms import RegistrationForm, PostForm
from application.user.models import Post
from application import app, db 
from flask_login import current_user, login_required
from datetime import date

post = Blueprint('tool', __name__)


@post.route("/post", methods=["GET", "POST"])
@login_required
def create_post_page():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, topic=form.topic.data, body=form.body.data, author_id=current_user.id, author_name=current_user.name, author_surname=current_user.surname, private=form.private.data, publication_date=date.today(), latest_editing_date=date.today())
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created!', 'success')
		return redirect(url_for('home.home_page'))
	return render_template('create_post.html', form=form)


@post.route("/edit_<post_>", methods=["GET", "POST"])
@login_required
def edit_post_page(post_):
	form = PostForm()
	form.make(post)

	if form.validate_on_submit():
		post = Post.query().get(post_.id)
		post.title = form.title.data
		post.topic = form.topic.data
		post.body = form.body.data
		post.private = form.private.data
		post.latest_editing_date = date.today()
		db.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('home.home_page'))
	return render_template('edit_post.html', form=form)

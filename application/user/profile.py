from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.forms import RegistrationForm, LoginForm
from application.user.models import User, Post
from application import app, db 
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc, asc

profile = Blueprint('profile', __name__)

@profile.route("/profile")
@profile.route("/profile_<post_num_begin_>")
@login_required
def profile_page(post_num_begin_=0):
	return render_template("profile.html", user=current_user, post_num_begin=int(post_num_begin_), 
		post_num_end=min(int(post_num_begin_) + 5, buf := Post.query.filter_by(author_id=current_user.id).order_by(asc(Post.publication_date)).count()),
		post_num_all=buf, 
		posts=Post.query.filter_by(author_id=current_user.id).order_by(asc(Post.publication_date)).all())


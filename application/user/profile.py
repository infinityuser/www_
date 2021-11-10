from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.forms import RegistrationForm, LoginForm
from application.user.models import User, Post
from application import app, db 
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc, asc

profile = Blueprint('profile', __name__)

@profile.route("/profile")
@login_required
def profile_page():
	return render_template('profile.html', user=current_user, posts=Post.query.filter_by(author_id=current_user.id).order_by(asc(Post.publication_date)).all())

'''
@profile.route("/change_profile")
@login_required
def change_profile():
	return render_template('profile.html', user=current_user)
'''	

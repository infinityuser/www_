from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.models import Post
from sqlalchemy import asc, desc

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
@home.route("/home_<post_num_begin_>")
def home_page(post_num_begin_=0):
	return render_template("home.html", post_num_begin=int(post_num_begin_), 
		post_num_end=min(int(post_num_begin_) + 1, buf := Post.query.filter_by(private=False).order_by(asc(Post.publication_date)).count()),
		post_num_all=buf, 
		posts=Post.query.filter_by(private=False).order_by(asc(Post.publication_date)).all())

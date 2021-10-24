from flask import Blueprint, render_template, url_for, flash, redirect, request
from application.user.models import Post
from sqlalchemy import asc, desc

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
def home_page():
	return render_template("home.html", posts=Post.query.filter_by(private=False).order_by(asc(Post.publication_date)).all())

@home.route("/about")
def info_page():
	return "Here is an info"

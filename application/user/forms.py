from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import TextArea
from application.users.models import Post


class RegistrationForm(FlaskForm):
	name = StringField('Name',
						validators=[DataRequired(), Length(min=2, max=20)])
	surname = StringField('Surname',
						validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[DataRequired(), Email(), Length(min=2, max=120)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=60)])
	confirm_password = PasswordField('Confirm Password',
						validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(min=2, max=120)])
	topic = StringField('Topic', validators=[DataRequired(), Length(min=2, max=30)])
	body = StringField('Text', widget=TextArea(), validators=[DataRequired(), Length(min=10, max=5000)])
	private = BooleanField('Private')
	submit = SubmitField('Post')

	def make(self, post):
		self.title = post.title
		self.topic = post.topic
		self.body = post.body
		self.private = post.private
		

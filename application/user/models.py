from application import login_manager, db, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	surname = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	profile_picture = db.Column(db.String(130), nullable=False)
	permissions = db.Column(db.String(60), nullable=False)

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.name}', '{self.surname}', '{self.email}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, nullable=False)
	author_name = db.Column(db.String(20), nullable=False)
	author_surname = db.Column(db.String(20), nullable=False)
	private = db.Column(db.Boolean, nullable=False)
	title = db.Column(db.String(120), unique=True, nullable=False)
	topic = db.Column(db.String(30), nullable=False)
	body = db.Column(db.Text, nullable=False)
	publication_date = db.Column(db.Date, nullable=False)
	latest_editing_date = db.Column(db.Date, nullable=False)

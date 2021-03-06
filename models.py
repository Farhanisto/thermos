from datetime import datetime
from sqlalchemy import desc
from thermos import db

class Bookmark(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	url=db.Column(db.Text,nullable=False)
	date=db.Column(db.DateTime,default=datetime.utcnow)
	description=db.Column(db.String(300))
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

	@staticmethod
	def newest(num):

		return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)


	def __repr__(self):
		return "<Bookmark '{}':'{}'>".format(self.description,self.url)



class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	user=db.Column(db.String(80),unique=True)
	email=db.Column(db.String(80),unique=True)
	bookmark=db.relationship('Bookmark',backref='User',lazy='dynamic')


	def __repr__(self):
		return "<Bookmark %r"%self.user
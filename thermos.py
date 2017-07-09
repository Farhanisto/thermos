from flask import Flask,render_template,url_for,request,redirect,flash
from datetime import datetime
from Forms import BookmarkForm
from flask_sqlalchemy import SQLAlchemy
import os
import models


baseddir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY']='\xa2}{a9\xf8\x08-\x92 \xcb\x81E\xc7/\xd9\x9a\x9b\xa2^\xb4 !A'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(baseddir,'thermos.db')
db=SQLAlchemy(app)



bookmark=[]


class User:
	def __init__(self,fn,ln):
		self.fn=fn
		self.ln=ln

	def initial(self):
		return "{} {}".format(self.fn,self.ln)





#def new_bookmarks(num):
#	return sorted(bookmark,key=lambda bm: bm['date'],reverse=True)[:num]


	
	

@app.route("/")

def index():
	return render_template('index.html',new_bookmarks=models.Bookmark.newest(5))

@app.route("/add",methods=["POST","GET"])

def add():
	form=BookmarkForm()


	if form.validate_on_submit():

		url=form.url.data
		description=form.description.data
		bm=models.Bookmark(url=url,description=description)
		db.session.add(bm)

		db.session.commit()


		flash("Your bookmark has been saved '{}'".format(description))
		return redirect(url_for('index'))

	return render_template('add.html',form=form)

@app.errorhandler(404)
def errorHandler(e):
	return render_template('404.html'),404


if __name__=='__main__':
	app.run(debug=True,port=7000)





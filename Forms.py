from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired,url

class BookmarkForm(Form):
	url=URLField('enter your URL',validators=[DataRequired(),url()])
	description=StringField('description')

	'''def validate(self):
		if not self.url.data.startswith('http') or\
		 self.url.data.startswith('https'):

			self.url.data='http://' + self.url.data

		if not Form.validate:
			return False

		if not self.description.data:
			self.description.data=self.url.data

		return True'''




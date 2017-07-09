from models import db,User
from thermos import app
from flask_script import Manager,prompt_bool

manager=Manager(app)
@manager.command
def initdb():
    db.create_all()
    db.session.add(User(user='farhan', email='farhanisto@gmail.com'))
    db.session.commit()



    print "Db created"



@manager.command
def dropdb():
    if prompt_bool("Are you sure ?"):
        db.drop_all()
        print "Db dropped"

if __name__=='__main__':

    manager.run()




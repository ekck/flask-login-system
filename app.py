from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SECRET_KEY']='616919'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

login_manager= LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))


@login_manager.user_loader
def get(id):
    return User.query.get(id)

@app.route('/',methods=['GET'])
#@login_required
def get_home():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
#@login_required
def get_login():
    return render_template('login.html')

#@app.route('/')
#def get():
#    return 'ok'





if __name__=='__main__':
    app.run(debug=True)
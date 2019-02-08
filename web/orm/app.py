from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
from models import db, User
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# flask app 에 sqlalchemy 관련설정
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db_flask.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# sqlalchemy데이터 베이스 객체 수정 및 신호 발송들을 추적 , 과도한 메모리를 사용하기 때문애 False

# sqlalchemy초기화
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)
    
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username = username, email = email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user = user)
    
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    user.username = username
    user.email = email
    db.session.commit()
    return redirect(url_for('index', id=id))
    
    
    

if __name__ == '__main__':
    app.run(host = os.getenv('IP'), port = os.getenv('PORT'), debug = True)
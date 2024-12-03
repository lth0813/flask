from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL / MariaDB 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/flask'
# 경고 제거
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# 데이터베이스 초기화
with app.app_context():
    db.create_all()

# CRUD 구현
@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"{username}님의 정보가 DB에 저장되었습니다."

@app.route('/users')
def get_user():
    users = User.query.all()
    return '<br>'.join([f"ID: {user.id}, Name: {user.username}, Email: {user.email}" for user in users])
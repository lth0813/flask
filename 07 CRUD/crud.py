from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()

# Create
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return {"message": "회원이 등록되었습니다."}

# Read
@app.route('/read', methods=['GET'])
def read():
    users = User.query.all()
    return [{"ID": user.id, "UserName": user.username, "Email": user.email} for user in users]

# Update
@app.route('/update/<int:user_id>', methods=['PUT'])
def update(user_id):
    # 특정 사용자 검색
    user = User.query.get(user_id)
    if not user:
        return {"error" : "회원정보를 찾을 수 없습니다."}, 404
    
    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()

    return {"message" : "회원정보가 수정되었습니다.", "user" : {"ID": user.id, "UserName": user.username}}

# Delete
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error" : "회원정보를 찾을 수 없습니다."}, 404
    
    db.session.delete(user)
    db.session.commit()

    return {"message": "해당 회원이 삭제되었습니다."}

if __name__ == '__main__':
    app.run(debug=True)
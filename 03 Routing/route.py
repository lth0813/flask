from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Spring Boot의 @RestController와 유사하지만 Flask에서는 메서드 타입을 따로 지정하지 않으면 기본적으로 GET 요청
@app.route('/about')
def about():
    return "This is the About Page"

# URL 경로에 변수를 추가 가능
@app.route('/user/<username>')
def profile(username):
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
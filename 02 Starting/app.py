from flask import Flask

# Flask 앱을 생성
app = Flask(__name__)

# URL 라우팅 설정, Spring Boot의 @GetMapping("/")과 유사
@app.route('/')
def home():
    return "Hello, Flask!"

# 개발 모드로 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# 동적 데이터 전달
def home():
    # String 데이터 전달
    fruits = 'Apple'
    # fruit 라는 이름으로 데이터 전달
    return render_template('fruitsBasket.html', fruit=fruits)

@app.route('/home2')
def home2():
    # List 데이터 전달
    fruits = ['Apple', 'Banana', 'Grape']
    return render_template('fruitsBasket.html', fruit_list=fruits)

@app.route('/home3')
def home3():
    # Dictionary 데이터 전달
    user = {'name':'Kim', 'age':'30', 'gender':'Male'}
    return render_template('user.html', user_detail=user)

@app.route('/status')
def home4():
    # 동적 데이터 전달에서의 조건문
    status = True
    return render_template('login.html', status=status)
if __name__ == '__main__':
    app.run(debug=True)
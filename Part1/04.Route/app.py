# 라우팅(routing) 
# 경로로 들어오는 요청에 대해 응답을 리턴
from flask import Flask, request, Response

app = Flask(__name__)

# 기본 경로에 대한 라우트
@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "This is the about page!"

#동적으로 URL 파라미터 값을 받아서 처리해준다.
#http://127.0.0.1:5000/user/eunjae
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

@app.route('/number/<int:number>')
def number(number):
    return f'number : {number}'

#Post 요청 날리는 법
# (1) postman
# (2) requests
import requests # pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response.text

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)

    return Response("Sucessfully submitted", status=200) 

if __name__ == "__main__":
    app.run()



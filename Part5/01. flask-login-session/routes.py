# 라우팅, 블루프린트를 사용해서 url과 함수를 매핑하는 라우트역할
from flask import render_template, request, redirect, url_for, session
from models import User, users
from flask_login import login_user, login_required, logout_user

def configure_routes(app):
    # 메인
    @app.route('/')
    def index():
        return render_template('index.html')

    # 로그인(브라우저에서 ID, PW -> 서버)
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password =request.form['password']

            # models.py에서 username에 해당하는 유저정보를 찾은 결과(객체생성)
            # 즉, DB저장소인 users 딕셔너리에 키와 같음을 의미함.
            # User.get()은 User 클래스 안에 정의된 get() 정적 메서드 호출 후
            # get() 안에서 다시 User(user_id)를 호출하면서 **User 인스턴스(객체)**를 생성
            user = User.get(username) # 여기서 User 인스턴스 생성됨.

            # 유저정보를 찾은 결과와 username에 해당하는 사용자의 비밀번호를 확인
            # 브라우저에서 입력한 PW가 일치하면 
            if user and users[username]['password'] == password:
                login_user(user) # User 인스턴스를 세션에 저장
                print("세션 내용:", dict(session))  # 세션에 어떤 정보가 저장되어 있는지 확인
                return redirect(url_for('index'))

            else:
                flash('Invalid username or password')

        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        logout_user()   # 세션 종료
        session.clear() # 모든 세션 데이터 제거(쿠키 무력화)
        print("세션 내용:", dict(session))  # 세션에 어떤 정보가 저장되어 있는지 확인
        return redirect(url_for('index'))

    @app.route('/protected')
    @login_required # 로그인한 사용자만 접근
    def protected():
        return "<h1>Protected area</h1> <a href='/logout'>Logout</a>"



from flask import Flask
from flask_login import LoginManager
from models import User
from routes import configure_routes

app = Flask(__name__)
app.secret_key = 'flask-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 브라우저가 로그인된 상태일 때(첫번째 객체생성) → 다음 요청부터는 Flask가 자동으로 쿠키에 저장된 사용자 ID를 읽어서
# 이 load_user(user_id) 함수로 전달함 → 
# 그 아이디로 다시 User.get(user_id) 호출해서(로그인된 사용자가 이후 요청을 보낼 때) 유저 객체(두번째 객체생성)를 만들어줘요.
# 그렇게 해서 유저 객체가 세션에 다시 연결됩니다.
@login_manager.user_load
def load_user(user_id):
    return User.get(user_id) # 로그인 된 사용자가 이후 요청을 보낼 때, 여기서 또 User 인스턴스 생성 (2번째)

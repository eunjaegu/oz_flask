from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user import User

user_bp = Blueprint('user', __name__)

# 임시 사용자 데이터
users = {
    'user1': User('1', 'user1', 'pw123'),
    'user2': User('2', 'user2', 'pw123')
}

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    # post
    if request.method == 'POST': 
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = users.get(username)
        if user and user.password == password:
            # 액세스 토큰으로 관리
            access_token = create_access_token(identity=username)
            # 세션 및 토큰 기간 만료시 리프레시 토큰으로 액세스 토큰을 재발급
            refresh_token = create_refresh_token(identity=username)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    # get
    else: 
        return render_template('login.html')


@user_bp.route('/protected', methods=['GET'])
@jwt_required() # 인증되지 않은 사용자의 접근 막기
def protected():
    current_user = get_jwt_identity() #  현재 jwt를 갖고 있는 사람의 정보를 알 수 있다.
    return jsonify(logged_in_as=current_user), 200 # 이 유저로 현재 접속했다.

@user_bp.route('/protected_page')
def protected_page():
    return render_template('protected.html')

# 로그아웃
from flask_jwt_extended import get_jwt
from blocklist import add_to_blocklist  # 블랙리스트 관리 모듈 임포트
@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"] # 여러 토큰 중 나의 토큰을 가져와 변수에 담은 후
    add_to_blocklist(jti)  # jti를 블랙리스트에 추가
    return jsonify({"msg": "Successfully logged out"}), 200
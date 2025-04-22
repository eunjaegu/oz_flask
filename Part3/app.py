from flask import Flask, render_template
from flask_smorest import Api
from db import db
from models import User, Board


app = Flask(__name__)

#SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)

#blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.board import board_blp
from routes.users import user_blp
api.register_blueprint(board_blp)
api.register_blueprint(user_blp) 


@app.route('/manager-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manager-users')
def manage_users():
    return render_template('users.html')

# 모델에 테이블이 생성되어있지 않으면 테이블 자동 생성
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # 데이터베이스 생성
        #db.drop_all()

    app.run(debug=True)       
#0.  Flask 애플리케이션과 Flask-Smorest API의 기본 설정을 포함합니다. Swagger UI 경로도 설정됩니다.
#1. Flask 앱 객체 생성
#2. OAS Swagger UI 설정
#3. Flask 앱에 api 기능 추가
#4. 만든 Blueprint 객체 등록
#5. 서버 실행

from flask import Flask
from flask_smorest import Api
from api import book_blp

# Flask 엡 객체 생성
app = Flask(__name__)

#OAS(Open Api Specification) - Swagger UI
#Swagger UI에 보일 API 문서 제목
app.config["API_TITLE"] = "My API" 

# API 버전
app.config["API_VERSION"] = "v1" 

# 사용할 OpenAPI 스펙 버전(Swagger와 호환되는 명세)
app.config["OPENAPI_VERSION"] = "3.1.3" 

# OpenAPI 문서의 URL 접두사 → 기본 루트로 설정되어 있으므로 /swagger-ui가 완전한 주소로 됨
app.config["OPENAPI_URL_PREFIX"] = "/" 

# Swagger UI가 열리는 경로 /  접속 주소: http://127.0.0.1:5000/swagger-ui
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" 

#Swagger UI에 필요한 프론트엔드 리소스를 CDN으로 불러옴
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" 

# Flask 애플리케이션에 Smorest API 기능을 추가
api = Api(app)

# app.py 파일에서 만든 blp Blueprint 객체 등록
# 이 안에는 /items/, /items/<int:item_id> 등 다양한 경로가 있음
api.register_blueprint(book_blp)

# 이 파일 직접 실행 시 서버 실행
# debug=True 코드 수정 시 자동 리로드 및 상세 에러 확인
if __name__ == '__main__':
    app.run(debug=True)


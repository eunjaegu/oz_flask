from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# RestAPI를 정렬해서 보여주는 툴
# OpenAPI 관련 설정
# 스웨거(Swagger) 문서 페이지 설정
# OAS(Open Api Specification) - Swagger UI
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
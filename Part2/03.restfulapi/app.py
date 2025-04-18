from flask import Flask
from flask_restful import Api
from resource.item import Item

app = Flask(__name__)

api = Api(app)

api.add_resource(Item, '/item/<string:name>') # 경로 추가 (클래스명, 원하는 주소)

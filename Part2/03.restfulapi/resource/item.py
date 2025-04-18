from flask import request
from flask_restful import Resource


items = [] # DB의 대체 역할 (간단한 DB 역할)

# Resource : MethodView
class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg":"Item not found"}, 404 # msg, code     

    #아이템 생성
    def post(self, name):
        #동일한 이름의 아이템 존재 여부 확인
        for item in items:
            if item['name'] == name:
                return {"msg":"Item Already exists"}, 400 #중복이면 400 반환
            
        # 클라이언트로부터 JSON 데이터 받음    
        data = request.get_json()

        # 새로운 아이템 생성
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)

        return new_item # 생성한 아이템 반환

    
    #아이템 업데이트
    def put(self, name):
        #JSON 데이터 받기
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                # 이름이 존재하는 경우 : 가격만 수정
                item['price'] = data['price']
                return item
            
        # 만약, 이름이 존재하지 않는 경우 : 업데이트하고자하는 아이템 데이터가 없다면 -> 추가한다.
        new_item = {'name':name, 'price':data['price']}  
        items.append(new_item)

        return new_item
    
    #아이템 삭제
    def delete(self, name):
        global items
        # 해당 name이 아닌 아이템만 남기고 필터링
        items = [item for item in items if item['name'] != name]

        return {"msg":"Item Deleted"}
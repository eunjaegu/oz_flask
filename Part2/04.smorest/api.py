from flask.views import MethodView
from flask_smorest import Blueprint, abort 
from schemas import ItemSchema

# 📌 Blueprint 객체 생성
# 'items'는 Blueprint의 이름 (나중에 등록할 때 사용됨)
# URL prefix는 '/items'로 지정 => API 경로(접두사)가 /items/... 형태로 시작됨
blp = Blueprint("items", "items", url_prefix="/items", description="Operations on items")

# 📌 데이터를 저장할 임시 리스트 (DB 대신)
items = []

# 'ItemList' 클래스 - /items 경로에 대한 GET() 및 POST 요청을 처리(메서드 정의))
@blp.route("/")
class ItemList(MethodView):
    # GET 요청 시 응답 코드 200, 자동으로 JSON 반환
    @blp.response(200)
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return items

    # POST 요청에서 body를 ItemSchema로 검증해서 new_data로 전달
    # 요청으로 들어온 JSON 데이터를 검증하고, Python 객체로 변환해주는 데코레이터
    @blp.arguments(ItemSchema)
    @blp.response(201, description="Item added") # 응답 코드 201 및 문서화 설명
    def post(self, new_data):
        # 새 아이템을 추가하는 POST 요청 처리
        items.append(new_data)
        return new_data

# 'Item' 클래스 - GET, PUT, DELETE 요청을 처리
@blp.route("/<int:item_id>")
class Item(MethodView):
    @blp.response(200)
    def get(self, item_id):
        # 특정 ID를 가진 아이템을 반환하는 GET 요청 처리
				# next() => 반복문에서 값이 있으면 값을 반환하고 없으면 None을 반환
				# next는 조건을 만족하는 첫 번째 아이템을 반환하고, 그 이후의 아이템은 무시합니다.
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        return item

    #요청으로 들어온 JSON 데이터를 검증하고, Python 객체로 변환해주는 데코레이터
    @blp.arguments(ItemSchema)
    #응답
    @blp.response(200, description="Item updated")
    def put(self, new_data, item_id):
        # 특정 ID를 가진 아이템을 업데이트하는 PUT 요청 처리
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        item.update(new_data)
        return item

    @blp.response(204, description="Item deleted")
    def delete(self, item_id):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global items

        # any : 하나라도 True면 True, 모두 False면 False를 리턴하는 함수
        # 삭제할 ID가 존재하지 않으면 -> 에러 보내라.
        if not any(item for item in items if item["id"] == item_id):
            abort(404, message="Item not found")

        # 지정된 ID의 아이템 삭제
        # 새 리스트 생성 후 나머지는 items 변수에 담기
        items = [item for item in items if item["id"] != item_id]
        return ''
    


from marshmallow import Schema, fields

class ItemSchema(Schema):
		# id 필드가 직렬화(즉, Python 객체에서 JSON으로 변환) 과정에서만 사용되고, (서버->클라)
		# 역직렬화(즉, JSON에서 Python 객체로 변환) 과정에서는 무시된다 (클라->서버)
		# 즉, id 값은 서버에서 관리하겠다는 뜻

    # id는 클라이언트가 보낼 필요 없음 → 서버가 자동 생성 (출력할 때만 보여줌)
    id = fields.Int(dump_only=True)  
    # name은 필수로 받아야 함 (예: POST/PUT에서)
    name = fields.Str(required=True)
    # description은 선택사항
    description = fields.Str()
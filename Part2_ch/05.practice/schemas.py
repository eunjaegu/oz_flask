#0. 책 정보를 위한 스키마를 정의합니다. 여기서는 책의 제목과 저자가 필요하며, 책의 고유 ID는 자동으로 설정됩니다.
#1. 책정보를 처리할 스키마 클래스 작성

from marshmallow import Schema, fields
# 마시멜로의 기본 스키마 클래스. 여기에 어떤 필드가 필요한지 정의해서 사용
# 각 필드(데이터 항목)의 타입을 지정할 때 사용 (문자열, 숫자, 리스트 등)

#BookSchema는 책 정보를 처리할 때 사용하는 스키마 클래스
class BookSchema(Schema):
    #title, author: 문자열(String) 타입의 필드
    #required=True: 이 필드는 필수! 요청 데이터에 없으면 에러가 발생
    id = fields.Integer(dump_only=True)  # 클라이언트가 보낼 필요는 없음 (응답만 포함)
    title = fields.String(required=True)
    author = fields.String(required=True)
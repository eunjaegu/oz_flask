#0. 책 목록을 관리하는 API 엔드포인트를 구현합니다. GET, POST, PUT, DELETE 메소드를 사용하여 책 목록을 조회, 추가, 수정, 삭제할 수 있습니다.
#1. 블루프린트 객체 생성
#2. 데이터 저장소 생성
#3. 엔드포인트 구현(GET, POST, PUT, DELETE)

from flask_smorest import Blueprint, abort
from schemas import BookSchema
from flask.views import MethodView

# (블루프린트 이름(Swagger 문서 그룹 이름, 구분용), import할 때 모듈이름 처럼쓰이는 이름('books' 또는 __name__), api경로 앞에 /books, Swagger문서에 표시될 설명)
book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

# 엔드포인트 구현..
#GET, POST, PUT, DELETE 같은 실제 **API 기능(엔드포인트)**을 정의
#예: /books/<int:book_id> 같은 경로에 대한 클래스/메서드를 정의할 
@book_blp.route('/')
class BookList(MethodView) :
    #many=True : 전체 데이터 조회
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
            return books
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
            new_data['id'] = len(books) +1
            print(new_data['id'])
            books.append(new_data)
            return new_data

@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book

    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''



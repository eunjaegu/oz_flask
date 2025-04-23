# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db

# 테이블 명
# 실제 DB에 생성될 테이블 구조를 정의합니다.
# flask db migrate / upgrade 등을 통해 DB 테이블 생성 및 수정 가능.
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic') # 역참조

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')


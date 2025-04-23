#Flask-Login에서 제공하는 UserMixin
#UserMixin은 로그인 관련 기능 (is_authenticated, is_active, is_anonymous, get_id() 등)을 자동으로 제공해주는 믹스인 클래스
from flask_login import UserMixin

users = {'admin': {'password': 'pw123'}}

# Flask-Login 인증처리를 위한 클래스로
# Part3 /orm_sqlalchemy에서 models.py는 SQLAlchemy모델로, DB테이블과 연결됨.
class User(UserMixin):
    def __init__(self, username): # 생성자 메서드
        self.id = username  # 사용자 식별 id를 username으로 설정

    # 정적메서드: 클래스 내부에 정의되지만,인스턴스를 생성하지 않아도 호출 가능한 메서드
    # 인스턴스를 만들기 전에 user_id로 유저를 찾고 싶을 때 → 정적 메서드 적합!
    # 로그인 안헀을 때도 user_id가 필요한 이유? => 로그인 시 DB에 저장된 ID인지 확인을 위해
    # 로그인 안 한 상태에서 유저를 찾기 때문에 self가 없음(인스턴스가 없기때문이다.)
    @staticmethod 
    def get(user_id):
        # users 저장소에서 user_id가 존재하는지 확인
        if user_id in users:
            # User 클래스의 인스턴스를 생성해서 반환
            return User(user_id)

        return None

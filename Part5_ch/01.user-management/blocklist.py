# 블록리스트(토큰) 관리를 도와주는 파일
BLOCKLIST = set()


# Jwt를 관리하는 고유 넘버
def add_to_blocklist(jti):
    BLOCKLIST.add(jti)

# 블록리스트에서 discard를 지워주세요.
def remove_from_blocklist(jti):
    BLOCKLIST.discard(jti)
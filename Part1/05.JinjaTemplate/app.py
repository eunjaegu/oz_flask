# 라우팅(routing) 
# 경로로 들어오는 요청에 대해 응답을 리턴
# 요청이 들어오면 Jinja 템플릿을 사용하여 동적인 HTML 콘텐츠를 생성하고, 이를 브라우저에 응답하는 구조
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title' : 'Flask Jinja Template',
        'user' : 'eunjae',
        'is_admin' : True,
        'items_list' : ["Item1", "Item2", "Item3"]

    }

    # (1) redering 할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)


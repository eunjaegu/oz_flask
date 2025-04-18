# jsonify: Flask에서 Python 데이터를 JSON 형식으로 변환하여 HTTP 응답으로 반환할 때 사용되는 함수 

# 0. 서버가 실행되면,
# 1. Flask 애플리케이션 객체인 app이 생성
# 2. 그 이후 **각각의 @app.route**로 정의된 경로와 함수들이 app 객체에 등록
# 3. 이를 통해 URL 요청에 맞는 함수가 실행되는 구조

from flask import Flask, jsonify, request

# Sprint(Java) : @RestController클래스
# 즉, Flask 애플리케이션 인스턴스 생성
# Flask는 클래스, Flask(__name__)으로 만든 app은 그 객체.
app = Flask(__name__)

#GET
#(1) 전체 게시글을 불러오는 API
#함수가 app 인스턴스 내부의 라우팅 테이블(Route Map)에 등록

#Sprint(Java) : @RequestMapping("/hello"), @GetMapping
@app.route('/api/v1/feeds', methods=['GET'])
#Sprint(Java) : public String hello()
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data

#(2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success', 'data':{"feed1":'data1'}}

    return data

#Post
#(1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    # 1. 폼 데이터에서 값 추출
    name = request.form['name']
    age = request.form['age']

    print(name, age)

    # 2. Json 형태로 응답
    return jsonify({'result':'success'})

datas = [{"internal_items": [{"name": "items1", "price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()
    print(request_data)

    # 브라우저에서 보내는 데이터 : client_items
    new_data = {'internal_items': request_data.get("client_items", [])}
    datas.append(new_data)

    return new_data, 201

# Sprint(Java) : SpringApplication.run(App.class, args)
# 파이썬 파일 실행 시작 -> 서버 실행
# 즉, 직접 실행했을 때만 Flask 서버 켜줘
if __name__=="__main__":
    app.run() # 서버실행
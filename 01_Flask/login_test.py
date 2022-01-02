from flask import Flask, jsonify, request, render_template
# jsonify : json파일 리턴용
# request : 실제 웹페이지를 클릭할 때 uri(url 뒤 파라미터값들) 사용하기 위함
# render_template : template 랜더링 함수

# 객체 생성
app = Flask(__name__, static_url_path='/static')


# 라우팅
@app.route('/login')
def login():
    # get 방식으로 http 요청
    # html의 input태그의 name으로 데이터를 받는다.
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print(email_address, passwd)
    
    if email_address == 'ksk3083@naver.com':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081")

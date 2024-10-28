from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/baseball')
def baseball():
    return 'Hello, baseball!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        return "POST로 전달"
keyword = request.form["keywork"]
print(keywrod):
return f'POST로 전달된 당신이 입력한 검색어!' {keyword}
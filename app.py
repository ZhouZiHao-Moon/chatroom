from flask import Flask, request
import time
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    file = open('index.html', 'r', encoding='utf-8')
    html = file.read()
    file.close()
    return html


@app.route('/send/', methods=['POST'])
def send():
    with open('data/test/i.txt', 'r') as file:
        i = file.read()
    with open('data/test/i.txt', 'w') as file:
        file.write(str(int(i) + 1))
    file = open('data/test/'+str(i)+'.txt', 'w')
    file.write(request.form.get('name'))
    file.write('\n')
    file.write(request.form.get('text'))
    file.write('\n')
    file.write(request.form.get('time'))
    file.write('\n')
    file.close()
    return i


@app.route('/refresh/', methods=['GET', 'POST'])
def refresh():
    start = request.form.get('time')
    with open('data/test/i.txt', 'r') as file:
        finish = file.read()
    returndata = [{'name': '', 'time': finish, 'text': ''}]
    for i in range(int(start), int(finish)):
        filename = 'data/test/'+str(i)+'.txt'
        try:
            with open(filename, 'r') as fp:
                data = {
                    'name': fp.readline(),
                    'text': fp.readline(),
                    'time': fp.readline(),
                }
                returndata.append(data)
        except:
            pass
    return json.dumps(returndata)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14251, threaded=True)

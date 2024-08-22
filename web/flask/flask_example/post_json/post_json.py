from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/data/message/json', methods=['POST'])
def setDataMessageJson():
    if request.method == "POST":
        # 读取JSON格式的请求数据
        data = request.get_json()
        print("Received JSON data: ", data)
        return jsonify(data)


if __name__ == '__main__':
    app.run()

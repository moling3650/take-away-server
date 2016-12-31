import json
from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder='dist/static', template_folder='dist')

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

with open('data.json', encoding='utf-8') as reader:
    data = json.loads(reader.read())

@app.route('/api/seller')
def api_seller():
    return jsonify(errno=0, data=data['seller'])


@app.route('/api/goods')
def api_goods():
    return jsonify(errno=0, data=data['goods'])


@app.route('/api/ratings')
def api_ratings():
    return jsonify(errno=0, data=data['ratings'])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

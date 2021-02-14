from flask import Flask

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    return {
        'title': "React flask link APP",
        'mode': 'test'
    }

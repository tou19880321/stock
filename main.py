from flask import Flask

app = Flask(__name__)
print('test')

@app.route('/')
def hello_world():
    return 'Flask Dorized'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6090)
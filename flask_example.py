from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "OK"

@app.route('/1')
def test1page():
    return "page 1 ok"

@app.route('/2')
def test2page():
    return "page 2 ok"

def main():
    app.run(debug=True, port=8080)

if __name__ == '__main__':
    main() 

# local( my computer): development/testing
# webserver (remote / production)

# pacakge , library
# API -> application programming 
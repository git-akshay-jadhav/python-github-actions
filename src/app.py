from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my Flask web application!'

@app.route('/about')
def about():
    return 'This is a simple Flask web application created for demonstration purposes.'

if __name__ == '__main__':
    app.run(debug=True)

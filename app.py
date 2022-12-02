from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resp = make_response(render_template('index.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("landing page loaded")
    return resp

@app.route('/login')
def login():  # put application's code here
    resp = make_response(render_template('login.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("login page loaded")
    return resp

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, make_response, request

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

@app.route('/loginCheck', methods=["GET", "POST"])
def loginCheck():  # put application's code here
    UserName = request.args.get('email')
    pswd = request.args.get('pwd')
    print(UserName)
    print(pswd)
    if (UserName=="user@bot.com" and pswd=="temp1234"):
        resp = make_response(render_template('success.html'))
        return resp
    else:
        resp = make_response(render_template('error.html'))
        return resp

if __name__ == '__main__':
    app.run()

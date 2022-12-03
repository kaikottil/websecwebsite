from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = make_response(render_template('index.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("landing page loaded")
    return resp

@app.route('/login')
def login():
    resp = make_response(render_template('login.html'))
    resp.headers['X-XSS-Protection'] = '0'
    print("login page loaded")
    return resp

@app.route('/loginCheck', methods=["GET", "POST"])
def loginCheck():
    UserName = request.args.get('email')
    pswd = request.args.get('pwd')
    print(UserName)
    print(pswd)
    if (UserName=="user@bot.com" and pswd=="temp1234"):
        resp = make_response(render_template('item.html'))
        return resp
    else:
        resp = make_response(render_template('error.html'))
        return resp

@app.route('/checkbot', methods=["GET"])
def checkBot():
    resp = make_response(render_template('checkbot.html'))
    return resp

if __name__ == '__main__':
    app.run()

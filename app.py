import requests
import json
from flask import Flask, render_template, make_response, request
from flask import redirect, url_for
from time import time

app = Flask(__name__)
start_time = 0


def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """
    secret = "6LdiNFAjAAAAAO1cx2-ARSzhyRqYcqBu_RDYeEm6"
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


@app.route('/')
def hello_world():
    resp = make_response(render_template('index.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("landing page loaded")
    return resp


@app.route('/login')
def login():  # put application's code here
    resp = make_response(render_template('form.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("landing page loaded")
    return resp


@app.route('/loginpage', methods=["GET", "POST"])
def loginpage():  # put application's code here
    captcha_response = request.args.get('g-recaptcha-response')
    print(captcha_response)

    if is_human(captcha_response):
        # Process request here
        status = "Detail submitted successfully."
        resp = make_response(render_template('login.html'))
    else:
        # Log invalid attempts
        status = "Sorry ! Bots are not allowed."
        resp = make_response(render_template('error.html'))

    #resp = make_response(render_template('login.html'))
    # fix comment below line
    resp.headers['X-XSS-Protection'] = '0'
    print("login page loaded")
    print(status)
    return resp

@app.route('/loginCheck', methods=["GET", "POST"])
def loginCheck():
    UserName = request.args.get('email')
    pswd = request.args.get('pwd')
    print(request)
    if (UserName=="user@bot.com" and pswd=="temp1234"):
        return redirect(url_for('item'))
    else:
        resp = make_response(render_template('error.html'))
        return resp

@app.route('/item', methods=["GET"])
def item():
    global start_time

    start_time = time()
    resp = make_response(render_template('item.html'))
    return resp


@app.route('/checkbot', methods=["POST"])
def checkBot():
    global start_time

    time_elapsed = time() - start_time
    fingerprint = request.form['fingerprint']
    iswebdriver = request.form['webdriver']
    
    # Loading page where we process the information
    print(fingerprint)
    print(request.remote_addr)
    print(request.user_agent)
    print(iswebdriver)
    print(time_elapsed)

    resp = make_response(render_template('checkbot.html'))
    return resp


if __name__ == '__main__':
    app.run(debug=True)


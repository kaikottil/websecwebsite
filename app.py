from flask import Flask, render_template, make_response, request
import requests
import json

app = Flask(__name__)


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


@app.route('/loginPage', methods=["GET", "POST"])
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


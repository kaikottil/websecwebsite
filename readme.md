# BOT Detection techniques
This is a simple flask web application created to demonstrate the functionalities of our bot detection and prevention techniques. 
The website makes use of the following to detect bots:
- Captcha
- Browser fingerprinting
- IP tracking 
- Honeypot
- Response time 
- User Agent 

### Run Instructions

Install [python 3.9](https://www.python.org/downloads/release/python-390/) 

Install dependencies using the below command.
```
pip install -U Flask
```
Run the flask app using
```
python -m flask run
```
Access the website by opening [http://127.0.0.1:5000](http://127.0.0.1:5000) from your web browser. 

### Miscellaneous
- The captcha is registered and designed to work only from 127.0.0.1 for test purposes. Captcha will not load if you access the page using localhost. 
- The test user **email** is _user@bot.com_ and **password** is _temp1234_






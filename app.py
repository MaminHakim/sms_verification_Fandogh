from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
        
        return 'Hello'

@app.route('/v1/process')
def getsms():
        pass

def send_sms():
        pass

def check_serial():
        pass

if __name__ == "__main__":
        app.run("0.0.0.0, 5000")
        
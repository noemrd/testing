#testing
from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    user = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return render_template('hello.html', name=user)


app.run()

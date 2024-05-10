# flask web-based dashboard

from flask import FLask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bonjour, World!! Welcome to the system monitor dashboard'

if __name__ == '__main__':
    app.run(debug=True)
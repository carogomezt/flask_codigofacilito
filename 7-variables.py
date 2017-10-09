from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def index(name = 'Caro'):
    age = 17
    mlist = [1, 2, 3, 4]
    return render_template('user.html', nombre = name, edad = age, list = mlist)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def blank():
    return ('<h2>404 Server can not be found</h2>')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
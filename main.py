from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('success.html', message='You have already submitted the request')

if __name__ == '__main__':
    app.debug = True
    app.run()

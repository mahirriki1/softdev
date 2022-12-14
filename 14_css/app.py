from flask import Flask, render_template

app = Flask(__name__) # create flask object

@app.route('/') # route to home page
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
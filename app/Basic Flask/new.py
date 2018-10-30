from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    name = "Python Flask Workshop"
    return render_template('tmp.html', name1 = name)

if __name__ == '__main__':
    app.run(debug = True)



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def on_load():
    return render_template("index.html", num = 3)

@app.route('/play/<int:num>')
def add_squares(num):
    return render_template("index.html", num = num)

@app.route('/play/<int:num>/<string:color>')
def change_color(num,color):
    return render_template("index.html", num = num, color=color)

if __name__=="__main__":
    app.run(debug=True)

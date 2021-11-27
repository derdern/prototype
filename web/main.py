from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")

@app.route("/add_data")
def add_data():
    return render_template("add_data.html")

@app.route("/personal")
def personal():
    return render_template("personal.html")

@app.route("/morning")
def morning():
    return render_template("morning.html")


# if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8080, debug=True)

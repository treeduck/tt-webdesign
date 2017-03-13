import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template("index.html")

@app.route("/test")
def test():
    return flask.render_template("test.html")

if __name__ == "__main__":
    app.run()

# google map api key
# AIzaSyB66ikEGoIXGLPuvAaaD2zcOh8LB-SqCuk

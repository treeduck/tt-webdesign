import flask, os
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template("index.html")

@app.route("/test")
def test():
    return flask.render_template("test.html")

if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

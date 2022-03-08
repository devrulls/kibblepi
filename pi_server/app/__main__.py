from app import app


@app.route("/")
def hello_world():
    return "<p>Hello, you big fukin cat!</p>"


app.run()

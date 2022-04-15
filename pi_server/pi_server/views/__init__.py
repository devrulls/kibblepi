from pi_server import app


@app.route("/")
def index():
    return "Hello from Raspberry PI"

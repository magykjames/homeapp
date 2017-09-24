from homeapp import app


@app.route("/")
def home():
    return "Flask app running."

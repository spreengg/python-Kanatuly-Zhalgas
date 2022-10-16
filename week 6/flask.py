import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RRRRR"

if name == "__main__":
    app.run()

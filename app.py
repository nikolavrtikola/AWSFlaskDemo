from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Docker on AWS!What the Fuck am I doing...</h1>" \
    "<p>Test proba</p>" \
    "<h2>Da razberam sto se desava!!!</h2>"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
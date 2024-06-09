from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Is this my first flask app? i dont think so or do i think so? i dont know"
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)
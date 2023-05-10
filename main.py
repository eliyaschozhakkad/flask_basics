from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>welcome to the homepage</h1>"

@app.route("/addition",methods = ["POST"])
def addition():
    if request.method == "POST":
        num1 = request.json['num1']
        num2 = request.json['num2']

        result = num1 + num2

        return jsonify(f"The sum is {result}")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
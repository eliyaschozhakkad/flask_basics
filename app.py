from flask import Flask,request,render_template

app = Flask(__name__)

#Route
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return "We are iNeuron"

@app.route('/demo',methods = ['POST'])
def math_operaton():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        else:
            result = num1/num2

        return f"The operation is {operation} and the result is {result}"

@app.route('/operation',methods = ['POST'])
def operaton():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        else:
            result = num1/num2

        return render_template("result.html",result = result)


    




if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 5000)

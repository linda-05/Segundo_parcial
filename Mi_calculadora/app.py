from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            print(f"num1: {num1}, num2: {num2}, operacion: {operacion}")

            if operacion == "suma":
                result = num1 + num2
            elif operacion == "resta":
                result = num1 - num2
            elif operacion == "multiplicacion":
                result = num1 * num2
            elif operacion == "division":
                 if num2 == 0:
                     result = "Error: No se puede dividir por cero"
                 else:
                  result = num1 / num2
            else:
                error = "Operacion invalida"
        except ValueError:
            error = "Por favor ingrese numeros validos"

    print(f"result: {result}, error: {error}")
    
    return render_template("calculador.html", result= result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
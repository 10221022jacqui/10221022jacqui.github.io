from flask import Flask, render_template, request,url_for

app=Flask(__name__)


@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/resta', methods=['POST'])
def resta():
    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        try:
            r = int(n1) - int(n2)
            resultado ="El resultado es: " + str(r)
        except:
            resultado = "No se puede hacer la operación"
        return render_template('resultado.html', titulo="Resultado")
    else:
        return render_template('resta.html', titulo="Restar")


@app.route('/suma', methods=['POST'])
def suma():
    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        try:
            r = int(n1) + int(n2)
            resultado ="El resultado es: " + str(r)
        except:
            resultado = "No se puede hacer la operación"
        return render_template('resultado.html', titulo="Resultado")
    else:
        return render_template('suma.html', titulo="Sumar")
    
@app.route('/divicion', methods=['POST'])
def divicion():
    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        try:
            r = int(n1) / int(n2)
            resultado ="El resultado es: " + str(r)
        except:
            resultado = "No se puede hacer la operación"
        return render_template('resultado.html', titulo="Resultado")
    else:
        return render_template('divicion.html', titulo="Divicion")


@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        try:
            r = int(n1) * int(n2)
            resultado ="El resultado es: " + str(r)
        except:
            resultado = "No se puede hacer la operación"
        return render_template('resultado.html', titulo="Resultado")
    else:
        return render_template('multiplicacion.html', titulo="Multiplicacion")



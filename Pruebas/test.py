from flask import Flask
from flask import render_template
import a

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    name = "Koxme"
    s2 = "Peru"

    return render_template('index.html', name=name, name2=s2)

@app.route("/suma/<x>/<y>")
def sumaxy(x, y):
    return str(a.suma(x,y))


@app.route("/precio/<est1>/<est2>")
def precio(est1, est2):
    # calcular
    precio = str(2.5)
    return render_template('precio.html', precio=precio, est1=est1, est2=est2)



@app.route("/alumnos")
def lista_alumnos():
    lista_alumnos = ['Koxme', 'Peru', 'Mari']
    return render_template('alumnos.html', alumnos=lista_alumnos)


@app.route("/nombre/<s>")
def get_name(s):
    return render_template('index.html', name=s)


if __name__ == "__main__":
    app.run()
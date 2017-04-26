from flask import Flask, session
from flask import render_template
import misfunciones as rf


app = Flask(__name__)
app.debug = True
app.secret_key = 'A8Zr98j/1yX Z~XHH!jmN]LWX/,?LT'

opcion_seleccionada = ""

@app.route("/")
def principal():
    return render_template('Renfe.html')

@app.route("/opc/<select>")
def opc(select):
    stations = rf.print_stations()
    rf.opc = select
    return render_template('stations.html', stations=stations)
    session["<select>"] = select

@app.route("/precio/<station>")
def precio(station):

    zona_destino = rf.buscar_zona(station)
    precio_destino = rf.get_precio(zona_destino)
    return render_template('precio.html', precio=precio_destino, station=station, mipoblacion=rf.mipoblacion)


if __name__ == "__main__":
    app.run()


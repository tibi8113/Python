from flask import Flask
from flask import render_template
import misfunciones as rf


app = Flask(__name__)
app.debug = True

@app.route("/")
def principal():
    return render_template('Renfe.html')

@app.route("/opc/<select>")
def opc(select):
    stations = rf.print_stations()
    return render_template('stations.html', stations=stations)

@app.route("/precio/<station>")
def precio(station):
    precio = 1.6
    return render_template('precio.html', precio=precio, station=station, mipoblacion=rf.mipoblacion)


if __name__ == "__main__":
    app.run()


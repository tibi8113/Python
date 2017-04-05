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
    #return render_template('Renfe.html')
    #return "Has seleccionado la opción: " + select
    return str(rf.print_zonas())

if __name__ == "__main__":
    app.run()


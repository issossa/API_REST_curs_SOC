#!/usr/bin/python3
import flask
import json

app =flask.Flask(__name__)

@app.route("/precio/<v1>/<v2>")
def precio(v1, v2):
    precio_bruto = float(v1)
    porcentaje = float(v2)
    neto = ciento.Ciento(precio_bruto, porcentaje)
    resul = json.loads(str(neto))
    return flask.jsonify(resul)


def main():
    app.run()
    
if __name__ == "__main__":
    main()
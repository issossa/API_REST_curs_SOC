#!/usr/bin/python3

import flask      #flask es un framework
import json

app = flask.Flask(__name__)

@app.route("/suma/<n1>/<n2>")    # le damos una ruta y <n1> viene en texto
def suma(n1, n2):                # tenemos una función
    valor_v1 = float(n1)
    valor_v2 = float(n2)
    res = {"resultat": valor_v1 + valor_v2}
    return flask.jsonify(res)

@app.route("/resta")
def resta():
    body_text = flask.request.data # viene en text y lo pasa a tipo varible y en json será tipo diccionario
    body_dict = json.loads(body_text)
    return body_dict["n1"] + " " + body_dict["n2"]




def main():
    app.run()

if __name__ == "__main__":
    main()


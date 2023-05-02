#!/usr/bin/python3
import flask
import json
import porcentatge

app =flask.Flask(__name__)

@app.route("/calcula/<n1>/<n2>")
def calcula(n1, n2):
    valor_n1 = float(n1)
    valor_n2 = float(n2)
    operacio = porcentatge.Porcentatge(valor_n1,valor_n2)
    resul = operacio.calcula()
    return flask.jsonify(resul)


def main():
    app.run()
    
if __name__ == "__main__":
    main()
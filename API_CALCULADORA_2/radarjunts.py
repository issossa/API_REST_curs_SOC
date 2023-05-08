#!/usr/bin/python3
                     #junts en bloques
import flask
import json

app=flask.Flask(__name__)
@app.route("/speed/<coche>/<max>", methods=['GET'])
def velocity(coche, max):
    valor_coche=float(coche)
    valor_max=float(max)
    if valor_coche <= valor_max:
            lectura = "correcte"
        
    elif valor_coche<= 1.1*valor_max:
            lectura = "marge de seguretat"
        
    else:
            lectura = "multa"
    return flask.jsonify({"resultat":lectura})


def main():
    app.run() 

if __name__ == "__main__":
    main()

#!/usrbin/python3

import flask
import gos as gos
# import json no cal

app=flask.Flask(__name__) # constructor de una palicacion flask, llamando al init de flask

@app.route("/goscalcul/<n1>")
def gosanys(n1): #parametros llegan com string
    num=float(n1)  # lo decido yo o en funcion de la aplicacion

    gosguapo = gos.Gos(num)
    equivalencia = gosguapo.calcula() # invocar la funcion de la clase

    resultat = {"edad_del_perro": num, "equivalencia_humana": equivalencia}
    return flask.jsonify(resultat)

def main():
    app.run() 

if __name__ == "__main__":
    main()


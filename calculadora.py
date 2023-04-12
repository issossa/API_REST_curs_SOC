#!usr/bin/python3
import flask
app = flask.Flask(__name__)


@app.route('/suma/<a>/<b>')
def suma(a,b):
    return {"resultat ": int(a)+int(b)}


@app.route('/resta/<a>/<b>')
def resta(a,b):
    return {"resultat ": int(a)-int(b)}

@app.route('/multiplicacio/<a>/<b>')
def multiplicacio(a,b):
    return {"resultat ": int(a)*int(b)}


@app.route('/divisio/<a>/<b>')
def divisio(a,b):
    if int(b) == 0:
        return "", 400
    return {"resultat ": int(a)/int(b)}


if __name__ == "__main__":
    app.run()

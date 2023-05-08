
#!/usr/bin/python3
import flask
import radar

app=flask.Flask(__name__)
@app.route("/speed/<v1>/<v2>")
def velocitat(v1, v2):  
    valor_v1=float(v1) 
    valor_v2=float(v2)

    controla = radar.Radar(valor_v1, valor_v2) 
    valors = controla.calcula()
    resultat = {"valoración":valors}
    return flask.jsonify(resultat)

def main():
    app.run()

if __name__== '__main__':
    main()

from ast import Num
from flask import Flask 

app = Flask( __name__ )

@app.route( '/Dojo', methods=['GET'])

def paginaInicial():
    return "Dojo!"

@app.route( '/info/<nombre>', methods=['GET'])

def imprimeDatos( nombre ):
    return "Hola " + nombre

@app.route( '/repeat/<int:number>/<string:word>', methods=['GET'])

def repeat( number, word ):
    r = ""
    for i in range ( number ):
        r += f"{word} "

    return r
    
if __name__ == "__main__":
    app.run( debug=True )


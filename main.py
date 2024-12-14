from flask import  Flask, render_template, jsonify, request
 
carros=[
    {
        "id":"1",
        "marca":"mazda",
        "modelo":1983
    },{
        "id":"2",
        "marca":"honda",
        "modelo":1993
    }
]
 
#Datos iniciales de usuarios
usuario=[
    {
        "id":"1",
        "nombre":"Jennifer Gonzales",
        "email":"jenniferg@gmail.com"
    },{
        "id":"2",
        "nombre":"Pedro jimenez",
        "email":"Pjimenez@gmail.com"
    }
]

app = Flask(__name__)
 
@app.route("/")
def homme():
    return render_template("index.html")
 
@app.route("/carros", methods=["GET"])
def getcarros():
    return jsonify(carros)
 
@app.route("/carros", methods=["POST"])
def postcarros():
    nuevoCarro = request.json
    carros.append(nuevoCarro)
    return "nuevo carro creado"

@app.route("/carros/<id>", methods=["DELETE"])
def deletecarro (id):
    for car in carros:
        if car["id"] == id:
           carros.remove(car)
       
    return f"carro con id {id} a sido eliminado "
    return "id no econtrado"
 
@app.route("/carros/<id>", methods=["PUT"])
def putcarro (id):
    nuevocarro = request.json
    for carr in carros:
        if carr["id"] == id:
            ca = carros.index(carr)
            carros[ca] = nuevocarro
            return "carro actualizado"
    return "carro no econtrado"

app = Flask(__name__)
 
@app.route("/")
def homme():
    return render_template("index.html")
 
@app.route("/usuario", methods=["GET"])
def getusuario():
    return jsonify(usuario)
 
@app.route("/usuario", methods=["POST"])
def postusuario():
    nuevoUsuario = request.json
    usuario.append(nuevoUsuario)
    return "nuevo usuario creado"

@app.route("/usuario/<id>", methods=["DELETE"])
def deleteusuario (id):
    for us in usuario:
        if us["id"] == id:
           usuario.remove(us)
       
    return f"usuario con id {id} a sido eliminado "
    return "id no econtrado"
 
@app.route("/usuario/<id>", methods=["PUT"])
def putusuario (id):
    nuevoUsuario = request.json
    for usu in usuario:
        if usu["id"] == id:
            us = usuario.index(usu)
            usuario[us] = nuevoUsuario
            return "usuario actualizado"
    return "usuario no econtrado"



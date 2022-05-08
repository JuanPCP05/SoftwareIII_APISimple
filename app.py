from contextlib import nullcontext
import json
from flask import Flask, jsonify, request
from users import user

app = Flask(__name__)

index = 0

@app.route("/demo/register", methods=['POST'])
def register():
    global name
    global lang
    global index
    if request.method == 'POST':
        new_user = {
            "id": index,
            "name": request.json['name'],
            "lang": request.json['lang']
        }
        user.append(new_user)
    index += 1
    return jsonify({"message:": "Usuario registrado",
                    "Usuarios:": user})


@app.route("/demo/greeting/<string:name>")
def greeting(name):
    person = [u for u in user if u['name'] == name]
    if person is None:
        return 'Usuario no registradao'
    else:
        dict = person[0]
        print(person[0])
        if dict['lang'] == "ES":
            content = "Hola, " + dict['name'] +"!"
            return jsonify({"id:": dict['id'],
                    "content:": content})
        elif dict['lang'] == "EN":
            content = "Hello, " + dict['name'] +"!"
            return jsonify({"id:": dict['id'],
                    "content:": content})
        elif  dict['lang'] == "FR":            
            content = "Salut, " + dict['name'] +"!"
            return jsonify({"id:": dict['id'],
                    "content:": content})
        else:
            return "Error en el mensaje"        

if __name__ == '__main__':
    app.run(debug=True, port=5000)
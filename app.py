from flask import Flask, jsonify, request

app = Flask(__name__)

iniciais = [
    {
        "id": 1,
        "nome": "Iniciais Kanto",
        "items": [
            {
                "nome": "Bullbasaur",
                "tipo": "Planta/Venenoso"
            },
            {
                "nome": "Charmander",
                "tipo": "Fogo"
            },
            {
                "nome": "Squirtle",
                "tipo": "Água"
            }
        ],
    }, 
    {
        "id": 2,
        "nome": "Iniciais Johto",
        "items": [
            {
                "nome": "Chikorita",
                "tipo": "Planta"
            }, 
            {
                "nome": "Cyndaquil",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Totodile",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 3,
        "nome": "Iniciais Hoenn",
        "items": [
            {
                "nome": "Treecko",
                "tipo": "Planta"
            }, 
            {
                "nome": "Torchic",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Mudkip",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 4,
        "nome": "Iniciais Sinnoh",
        "items": [
            {
                "nome": "Turtwig",
                "tipo": "Planta"
            }, 
            {
                "nome": "Chimchar",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Piplup",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 5,
        "nome": "Unova",
        "items": [
            {
                "nome": "Snivy",
                "tipo": "Planta"
            }, 
            {
                "nome": "Tepig",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Oshawott",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 6,
        "nome": "Kalos",
        "items": [
            {
                "nome": "Chespin",
                "tipo": "Planta"
            }, 
            {
                "nome": "Fennekin",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Froakie",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 7,
        "nome": "Alola",
        "items": [
            {
                "nome": "Rowlet",
                "tipo": "Planta/Voador"
            }, 
            {
                "nome": "Litten",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Popplio",
                "tipo": "Água"
            }
        ],
    },
    {
        "id": 8,
        "nome": "Galar",
        "items": [
            {
                "nome": "Grookey",
                "tipo": "Planta"
            }, 
            {
                "nome": "Scorbunny",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Sobble",
                "tipo": "Água"
            }
        ],
    },  
    {
        "id": 9,
        "nome": "Paldea",
        "items": [
            {
                "nome": "Sprigatito",
                "tipo": "Planta"
            }, 
            {
                "nome": "Fuecoco",
                "tipo": "Fogo"
            }, 
            {
                "nome": "Quaxly",
                "tipo": "Água"
            }
        ]
    }
]


# GET /iniciais
@app.get('/iniciais')
def get_iniciais():
    return jsonify({"Iniciais": iniciais}), 200

# GET /iniciais/1
@app.get('/iniciais/<int:id>')
def get_iniciais_id(id):
    for inicial in iniciais: 
        if iniciais["id"] == id:
            return jsonify(iniciais), 200
    return jsonify({"erro": "Iniciais não encontrados"}), 404

# GET /iniciais?nome=XPTO
@app.get('/iniciais/nome')
def get_loja_name():
    nome = request.args.get('nome')
    for inicial in iniciais:
        if iniciais['nome'] == nome:
            return jsonify(iniciais), 200
    return jsonify({"erro": "Iniciais não encontrados"}), 404



if __name__ == "__main__":
    app.run(debug=True)

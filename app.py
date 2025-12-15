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
        if inicial["id"] == id:
            return jsonify(inicial), 200
    return jsonify({"erro": "Iniciais não encontrados"}), 404

# GET /iniciais?nome=XPTO
@app.get('/iniciais/nome')
def get_iniciais_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
    for inicial in iniciais:
        if inicial['nome'] == nome:
            return jsonify(inicial), 200
    return jsonify({"erro": "Iniciais não encontrados"}), 404

# POST /iniciais
@app.post('/iniciais')
def criar_iniciais():
    dado = request.get_json()
    if not dado: 
        return jsonify({"erro": "Dado não enviado"}), 400
    if "nome" not in dado: 
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400
    if "id" not in dado: 
        return jsonify({"erro": "O campo 'id' é obrigatório"}), 400

    if any(item['id'] == dado['id'] for item in iniciais):
        return jsonify({"erro": "ID já existe"}), 400

    novos_iniciais = {
        "id": dado['id'],
        "nome": dado['nome'],
        "items": dado.get("items", [])
    }

    iniciais.append(novos_iniciais)
    return jsonify(novos_iniciais), 201

# PUT /iniciais/<id_iniciais>
@app.put('/iniciais/<int:id_iniciais>')
def atualizar_iniciais(id_iniciais):
    dado_novo = request.get_json()
    if not dado_novo:
        return jsonify({"erro": "Dado não enviado"}), 400
    if 'nome' not in dado_novo: 
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400
    
    for inicial in iniciais:
        if inicial["id"] == id_iniciais:
            inicial['nome'] = dado_novo['nome']
            inicial['items'] = dado_novo.get('items', inicial['items'])
            return jsonify({"iniciais atualizada": inicial}), 200

    return jsonify({"erro": "Iniciais não encontrados"}), 404


if __name__ == "__main__":
    app.run(debug=True)
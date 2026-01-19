from flask import Flask, jsonify, request
import uuid
from db import regioes, pokemon

app = Flask(__name__)


# ============= REGIÕES =============

# GET /regioes — lista todas as regiões
@app.get('/regioes')
def listar_regioes():
    return jsonify({"Regiões": list(regioes.values())}), 200


# GET /regiao/<id_regiao> — busca região por id
@app.get('/regiao/<id_regiao>')
def buscar_regiao(id_regiao):
    if id_regiao not in regioes:
        return jsonify({"erro": "Região não encontrada"}), 404
    return jsonify(regioes[id_regiao]), 200


# GET /regiao?nome=XPTO — busca região por nome
@app.get('/regiao')
def buscar_regiao_por_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
    
    for regiao in regioes.values():
        if regiao.get('nome') == nome:
            return jsonify(regiao), 200
    
    return jsonify({"erro": "Região não encontrada"}), 404


# POST /regiao — cria região
@app.post('/regiao')
def criar_regiao():
    dado = request.get_json(silent=True)
    if not dado:
        return jsonify({"erro": "Dado não enviado"}), 400
    
    regiao_id = uuid.uuid4().hex
    nova_regiao = {**dado, "id": regiao_id}
    
    regioes[regiao_id] = nova_regiao
    
    return jsonify(nova_regiao), 201


# PUT /regiao/<id_regiao> — atualiza região
@app.put('/regiao/<id_regiao>')
def atualizar_regiao(id_regiao):
    if id_regiao not in regioes:
        return jsonify({"erro": "Região não encontrada"}), 404
    
    dado = request.get_json(silent=True)
    if not dado:
        return jsonify({"erro": "Dado não enviado"}), 400
    
    regioes[id_regiao].update(dado)
    
    return jsonify({"regiao atualizada": regioes[id_regiao]}), 200


# DELETE /regiao/<id_regiao> — deleta região
@app.delete('/regiao/<id_regiao>')
def deletar_regiao(id_regiao):
    if id_regiao not in regioes:
        return jsonify({"erro": "Região não encontrada"}), 404
    
    del regioes[id_regiao]
    
    return jsonify({"message": "Região removida com sucesso"}), 200


# ============= POKEMONS =============

# GET /pokemons — lista todos os pokemons
@app.get('/pokemons')
def listar_pokemons():
    return jsonify({"Pokemons": list(pokemon.values())}), 200


# GET /pokemon/<id_pokemon> — busca pokemon por id
@app.get('/pokemon/<id_pokemon>')
def buscar_pokemon(id_pokemon):
    if id_pokemon not in pokemon:
        return jsonify({"erro": "Pokemon não encontrado"}), 404
    return jsonify(pokemon[id_pokemon]), 200


# GET /pokemon?nome=XPTO — busca pokemon por nome
@app.get('/pokemon')
def buscar_pokemon_por_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
    
    for pokemon in pokemon.values():
        if pokemon.get('nome') == nome:
            return jsonify(pokemon), 200
    
    return jsonify({"erro": "Pokemon não encontrado"}), 404


# POST /pokemon — cria pokemon
@app.post('/pokemon')
def criar_pokemon():
    dado = request.get_json(silent=True)
    if not dado:
        return jsonify({"erro": "Dado não enviado"}), 400
    
    pokemon_id = uuid.uuid4().hex
    novo_pokemon = {**dado, "id": pokemon_id}
    
    pokemon[pokemon_id] = novo_pokemon
    
    return jsonify(novo_pokemon), 201


# PUT /pokemon/<id_pokemon> — atualiza pokemon
@app.put('/pokemon/<id_pokemon>')
def atualizar_pokemon(id_pokemon):
    if id_pokemon not in pokemon:
        return jsonify({"erro": "Pokemon não encontrado"}), 404
    
    dado = request.get_json(silent=True)
    if not dado:
        return jsonify({"erro": "Dado não enviado"}), 400
    
    pokemon[id_pokemon].update(dado)
    
    return jsonify({"pokemon atualizado": pokemon[id_pokemon]}), 200


# DELETE /pokemon/<id_pokemon> — deleta pokemon
@app.delete('/pokemon/<id_pokemon>')
def deletar_pokemon(id_pokemon):
    if id_pokemon not in pokemon:
        return jsonify({"erro": "Pokemon não encontrado"}), 404
    
    del pokemon[id_pokemon]
    
    return jsonify({"message": "Pokemon removido com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)
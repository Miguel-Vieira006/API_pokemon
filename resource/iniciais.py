from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request
from db import iniciais

iniciais_blp = Blueprint("iniciais", __name__, description="Operações de iniciais")


@iniciais_blp.route('/iniciais')
class IniciaisList(MethodView):

    def get(self):
        return jsonify({"Iniciais": iniciais}), 200

    def post(self):
        dados = request.get_json(silent=True)
        if not dados:
            return jsonify({"erro": "Dado não enviado"}), 400
        if 'nome' not in dados:
            return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

        new_id = max((i['id'] for i in iniciais), default=0) + 1
        novos = {**dados, "id": new_id}

        iniciais.append(novos)
        return jsonify(novos), 201


@iniciais_blp.route('/iniciais/nome')
class IniciaisByName(MethodView):

    def get(self):
        nome = request.args.get('nome')
        if not nome:
            return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
        for inicial in iniciais:
            if inicial['nome'] == nome:
                return jsonify(inicial), 200
        return jsonify({"erro": "Iniciais não encontrados"}), 404


@iniciais_blp.route('/iniciais/<int:id_iniciais>')
class IniciaisItem(MethodView):

    def get(self, id_iniciais):
        for inicial in iniciais:
            if inicial['id'] == id_iniciais:
                return jsonify(inicial), 200
        abort(404, message="Iniciais não encontrados")

    def put(self, id_iniciais):
        dado_novo = request.get_json(silent=True)
        if not dado_novo:
            return jsonify({"erro": "Dado não enviado"}), 400
        if 'nome' not in dado_novo:
            return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

        for inicial in iniciais:
            if inicial['id'] == id_iniciais:
                inicial['nome'] = dado_novo['nome']
                inicial['items'] = dado_novo.get('items', inicial.get('items', []))
                return jsonify({"iniciais atualizada": inicial}), 200

        abort(404, message="Iniciais não encontrados")

    def delete(self, id_iniciais):
        for inicial in iniciais:
            if inicial['id'] == id_iniciais:
                iniciais.remove(inicial)
                return jsonify({"message": "Iniciais removidos com sucesso"}), 200
        abort(404, message="Iniciais não encontrados")

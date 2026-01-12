from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request
from db import items
import uuid

item_blp = Blueprint("items", __name__, description="Operações de item")


@item_blp.route('/items')
class Items(MethodView):

    def get(self):
        return jsonify({"Itens": list(items.values())}), 200

    def post(self):
        item_dado = request.get_json(silent=True)
        if not item_dado:
            return jsonify({"erro": "Dado não enviado"}), 400

        item_id = uuid.uuid4().hex
        item_novo = {**item_dado, "id": item_id}

        items[item_id] = item_novo

        return jsonify(item_novo), 201


@item_blp.route('/items/<string:id_item>')
class ItemId(MethodView):

    def get(self, id_item):
        try:
            return jsonify(items[id_item]), 200
        except KeyError:
            abort(404, message="Item não encontrado")

    def put(self, id_item):
        dado = request.get_json(silent=True)
        if not dado:
            return jsonify({"erro": "Dado não enviado"}), 400
        if id_item not in items:
            abort(404, message="Item não encontrado")

        items[id_item].update(dado)
        return jsonify({"item atualizado": items[id_item]}), 200

    def delete(self, id_item):
        try:
            items.pop(id_item)
            return jsonify({"message": "Item removido com sucesso"}), 200
        except KeyError:
            abort(404, message="Item não encontrado")


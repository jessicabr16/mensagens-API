from flask import Blueprint, request, jsonify
import controllers

mensagem_bp = Blueprint("mensagem", __name__)

@mensagem_bp.route("/", methods=["POST"])
def criar():
    dados = request.get_json()
    nova = controllers.criar_mensagem(dados["conteudo"])
    return jsonify({"id": nova.id, "conteudo": nova.conteudo}), 201

@mensagem_bp.route("/", methods=["GET"])
def listar():
    mensagens = controllers.listar_mensagens()
    return jsonify([{"id": m.id, "conteudo": m.conteudo} for m in mensagens])

@mensagem_bp.route("/<int:id>", methods=["GET"])
def obter(id):
    msg = controllers.obter_mensagem(id)
    if msg:
        return jsonify({"id": msg.id, "conteudo": msg.conteudo})
    return jsonify({"erro": "Mensagem não encontrada"}), 404

@mensagem_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    msg = controllers.atualizar_mensagem(id, dados["conteudo"])
    if msg:
        return jsonify({"id": msg.id, "conteudo": msg.conteudo})
    return jsonify({"erro": "Mensagem não encontrada"}), 404

@mensagem_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    msg = controllers.deletar_mensagem(id)
    if msg:
        return jsonify({"mensagem": "Mensagem deletada"})
    return jsonify({"erro": "Mensagem não encontrada"}), 404

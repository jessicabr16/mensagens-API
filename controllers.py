from models import Mensagem
from database import db


def criar_mensagem(conteudo):
    nova = Mensagem(conteudo=conteudo)
    db.session.add(nova)
    db.session.commit()
    return nova

def listar_mensagens():
    return Mensagem.query.all()


def obter_mensagem(id):
    return Mensagem.query.all(id)

def atulizar_mensagem(id, novo_conteudo):
    msg = Mensagem.query.get(id)
    if msg:
        msg.conteudo = novo_conteudo
        db.session.commit()
        return msg

def deletar_mensagem(id):
    msg = Mensagem.query.get(id)
    if msg:
        db.session.delete(msg)
        db.session.commit()
        return msg
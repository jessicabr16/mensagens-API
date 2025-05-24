from flask import Flask
from database import db  # importa o db do database.py
from models import Mensagem
from routes import mensagem_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mensagens.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(mensagem_bp, url_prefix="/mensagens")

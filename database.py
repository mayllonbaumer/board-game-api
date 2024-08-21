from models import db, Game, Player, Match

def init_db():
    db.create_all()
    # Adicione dados de exemplo, se necessário

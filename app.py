import os
from flask import Flask, request, jsonify
from models import db, Game, Player, Match  # Importar os modelos e o objeto db
from database import init_db  # Se usar init_db para criar as tabelas

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com o app Flask
db.init_app(app)

# Inicializa o banco de dados (criação de tabelas) ao iniciar o contexto do app
with app.app_context():
    init_db()

@app.route('/games', methods=['GET', 'POST'])
def manage_games():
    if request.method == 'GET':
        games = Game.query.all()
        return jsonify([game.to_dict() for game in games])
    elif request.method == 'POST':
        data = request.json
        new_game = Game(
            title=data['title'],
            description=data['description'],
            photo_url=data['photoUrl'],
            players_min=data['playersMin'],
            players_max=data['playersMax'],
            rating=data['rating']
        )
        db.session.add(new_game)
        db.session.commit()
        return jsonify(new_game.to_dict()), 201

@app.route('/games/<int:game_id>', methods=['GET', 'PUT', 'DELETE'])
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == 'GET':
        return jsonify(game.to_dict())
    elif request.method == 'PUT':
        data = request.json
        game.title = data['title']
        game.description = data['description']
        game.photo_url = data['photoUrl']
        game.players_min = data['playersMin']
        game.players_max = data['playersMax']
        game.rating = data['rating']
        db.session.commit()
        return jsonify(game.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(game)
        db.session.commit()
        return '', 204

@app.route('/players', methods=['GET', 'POST'])
def manage_players():
    if request.method == 'GET':
        players = Player.query.all()
        return jsonify([player.to_dict() for player in players])
    elif request.method == 'POST':
        data = request.json
        new_player = Player(name=data['name'])
        db.session.add(new_player)
        db.session.commit()
        return jsonify(new_player.to_dict()), 201

@app.route('/matches', methods=['GET', 'POST'])
def manage_matches():
    if request.method == 'GET':
        matches = Match.query.all()
        return jsonify([match.to_dict() for match in matches])
    elif request.method == 'POST':
        data = request.json
        new_match = Match(game_id=data['gameId'], played_at=data['playedAt'])
        for player in data['players']:
            new_match.add_player(player['playerId'], player['score'])
        db.session.add(new_match)
        db.session.commit()
        return jsonify(new_match.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
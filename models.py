from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto db do SQLAlchemy sem o app
db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255))
    players_min = db.Column(db.Integer, nullable=False)
    players_max = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'photoUrl': self.photo_url,
            'playersMin': self.players_min,
            'playersMax': self.players_max,
            'rating': self.rating
        }

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    played_at = db.Column(db.DateTime, nullable=False)
    game = db.relationship('Game', backref=db.backref('matches', lazy=True))
    players = db.relationship('PlayerScore', backref='match', lazy=True)

    def add_player(self, player_id, score):
        self.players.append(PlayerScore(player_id=player_id, score=score))

    def to_dict(self):
        return {
            'id': self.id,
            'gameId': self.game_id,
            'playedAt': self.played_at,
            'players': [{'playerId': player.player_id, 'score': player.score} for player in self.players]
        }

class PlayerScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    player = db.relationship('Player', backref=db.backref('scores', lazy=True))
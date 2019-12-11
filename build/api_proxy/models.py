from app import db
import jwt
from config import SECRET_KEY
import datetime
class Worker(db.Model):
    __tablename__ = "workers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Worker name %r>' % self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    
    def __init__(self,email, password, admin=False):
        self.email= email
        self.password = password
        self.admin = admin
        
    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    worker_id =  db.Column(db.Integer, db.ForeignKey('workers.id'),
        nullable=False)
    volatility = db.Column(db.Float, nullable=False, default=0.0)
    shift = db.Column(db.Float, nullable=False, default=0.0)
    period = db.Column(db.Integer, nullable=False, default=0)
    duration = db.Column(db.Float, nullable=False, default=0)
    def __init__(self, user_id, worker_id, volatility, shift, period, duration):
        self.user_id = user_id
        self.worker_id = worker_id
        self.volatility = volatility
        self.shift = shift
        self.period = period
        self.duration = duration
    



    

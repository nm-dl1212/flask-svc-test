from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy インスタンスを作成
db = SQLAlchemy()

# ユーザーモデルの定義
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

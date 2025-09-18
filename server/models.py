from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'  

    serialize_rules = ('-updated_at',)

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now()   
    )
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(),  
        onupdate=lambda: datetime.now() 
    )

    def __repr__(self): 
        return f'<Message {self.id} | {self.username}: {self.body[:20]}...>'
from website import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    cartitems = db.relationship('Cart', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}', '{self.mobile}')"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(5), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    sub_category = db.Column(db.String(20), nullable=False)
    cartitems = db.relationship('Cart', backref='specificitem', lazy=True)


    def __repr__(self):
        return f"Item('{self.title}' , '{self.description}', '{self.price}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer,
                       db.ForeignKey('user.id'),
                       nullable=False,
                       )
    itemid = db.Column(db.Integer,
                       db.ForeignKey('item.id'),
                       nullable=False
                       )
    status = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f"Cart('{self.userid}', '{self.itemid} ,'{self.status}')"

from threading import Thread
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import mysql.connector
from backend.matcher import Match

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="oms"
)


class MyFlaskApp(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
            with self.app_context():
                Thread(target=Match).start()
        super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = MyFlaskApp(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mrig.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Securities(db.Model):
    security_name = db.Column(db.String(80), primary_key=True)
    isin = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    ltprice = db.Column(db.Integer)
    Orders = db.relationship('Order', backref='owner', lazy='dynamic')
    Rejected_Orders = db.relationship('Rejected_Order', backref='owner', lazy='dynamic')


def __init__(self, security_name, isin, type, ltprice):
    self.security_name = security_name
    self.isin = isin
    self.type = type
    self.ltprice = ltprice


class SecuritiesSchema(ma.Schema):
    class Meta:
        fields = ('security_name', 'isin', 'type', 'ltprice')


Security_Schema = SecuritiesSchema()
Securities_Schema = SecuritiesSchema(many=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    aon = db.Column(db.String(80), nullable=False)
    identifier = db.Column(db.Integer, nullable=False, default=0)
    BOS = db.Column(db.String(80), nullable=False, default='b')
    LOM = db.Column(db.String(80), nullable=False)
    Order_isin = db.Column(db.String(80), db.ForeignKey('securities.isin'))

    def __init__(self, Order_isin, price, qty, aon, identifier, BOS, LOM):
        self.Order_isin = Order_isin
        self.price = price
        self.qty = qty
        self.aon = aon
        self.identifier = identifier
        self.BOS = BOS
        self.LOM = LOM


class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id','Order_isin', 'price', 'qty', 'aon', 'identifier', 'BOS', 'LOM')


Order_Schema = OrderSchema()
Orders_Schema = OrderSchema(many=True)


class Rejected_Order(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    aon = db.Column(db.String(80), nullable=False)
    LOM = db.Column(db.String(80), nullable=False)
    BOS = db.Column(db.String(80), nullable=False)
    Order_isin = db.Column(db.String(80), db.ForeignKey('securities.isin'))

    def __init__(self, Order_isin, price, qty, aon, BOS, LOM):
        self.Order_isin = Order_isin
        self.price = price
        self.qty = qty
        self.aon = aon
        self.BOS = BOS
        self.LOM = LOM


class RejectedOrderSchema(ma.Schema):
    class Meta:
        fields = ('sr_no','Order_isin', 'price', 'qty', 'aon', 'BOS', 'LOM')


RejectedOrder_Schema = RejectedOrderSchema()
RejectedOrders_Schema = RejectedOrderSchema(many=True)


# endpoint to add a new security
@app.route("/security", methods=["POST"])
def add_security():
    security_name = request.json['security_name']
    isin = request.json['isin']
    type = request.json['type']
    ltprice = request.json['ltprice']

    new_security = Securities(security_name=security_name, isin=isin, type=type, ltprice=ltprice)
    db.session.add(new_security)
    db.session.commit()
    return Security_Schema.jsonify(new_security)


# endpoint to show all securities
@app.route("/securities", methods=["GET"])
def get_securities():
    global conn
    cur = conn.cursor()
    cur.execute("select * from Securities_Index;")
    temp = cur.fetchall()
    return jsonify(temp)


# endpoint to add a new Order
@app.route("/order", methods=["POST"])
def add_order():
    Order_isin = request.json['Order_isin']
    price = request.json['price']
    qty = request.json['qty']
    aon = request.json['aon']
    identifier = request.json['identifier']
    BOS = request.json['BOS']
    LOM = request.json['LOM']

    new_order = Order(Order_isin, price, qty, aon, identifier, BOS, LOM)
    db.session.add(new_order)
    db.session.commit()
    return Order_Schema.jsonify(new_order)


# endpoint to show all orders
@app.route("/orders", methods=["GET"])
def get_orders():
    global conn
    cur = conn.cursor()
    cur.execute("select * from Order_Index;")
    temp = cur.fetchall()
    return jsonify(temp)


# endpoint to add a new Rejected Order
@app.route("/Rejectedorder", methods=["POST"])
def add_Rejected_order():
    Order_isin = request.json['Order_isin']
    price = request.json['price']
    qty = request.json['qty']
    aon = request.json['aon']
    BOS = request.json['BOS']
    LOM = request.json['LOM']

    new_Rejected_order = Rejected_Order(Order_isin, price, qty, aon, BOS, LOM)
    db.session.add(new_Rejected_order)
    db.session.commit()
    return Order_Schema.jsonify(new_Rejected_order)


# endpoint to show all Rejected Orders
@app.route("/Rejectedorders", methods=["GET"])
def get_Rejected_orders():
    global conn
    # all_Rejected_orders = Order.query.all()
    # result = Orders_Schema.dump(all_Rejected_orders)
    cur = conn.cursor()
    cur.execute('''select * from Rejected_Order;''')
    result = cur.fetchall()
    return jsonify(result)


@app.route("/tradeindex", methods=["GET"])
def get_trade_index():
    global conn
    cur = conn.cursor()
    cur.execute('''select * from Trade_Index;''')
    result = cur.fetchall()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)

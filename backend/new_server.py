import pymysql
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import flash, request
import mysql.connector
from threading import Thread
import os
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

app = Flask(__name__)
CORS(app)


# endpoint to show all securities
@app.route('/securities', methods=['GET'])
def show_security():
    try:
        global conn
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Securities_Index;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add  securities
@app.route('/addsecurity', methods=['POST'])
def add_security():
    global conn
    try:
        _json = request.json
        _ISIN = _json['ISIN']
        _name = _json['name']
        _type = _json['type']
        _ltprice = _json['ltprice']

        if _ISIN and _name and _type and _ltprice and request.method == 'POST':
            sqlQuery = "INSERT INTO securities_index(ISIN,name,type,ltprice) VALUES(%s, %s, %s, %s);"
            bindData = (_ISIN, _name, _type, _ltprice)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Security added successfully!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to show all orders
@app.route('/orders', methods=['GET'])
def show_orders():
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Order_Index;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add orders
@app.route('/addorder', methods=['POST'])
def add_order():
    global conn
    try:
        _json = request.json
        _id = _json['id']
        _ISIN = _json['ISIN']
        _price = _json['price']
        _qty = _json['qty']
        _aon = _json['aon']
        _identifier = _json['identifier']
        _BOS = _json['BOS']
        _LOM = _json['LOM']

        if _ISIN and _id and _price and _qty and _identifier and _BOS and _LOM and request.method == 'POST':
            sqlQuery = "INSERT INTO order_index(id,ISIN,price,qty,aon,identifier,BOS,LOM) VALUES(%s, %s, %s, %s ,%s, %s, %s ,%s);"
            bindData = (_id, _ISIN, _price, _qty,_aon,_identifier, _BOS, _LOM)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Order added successfully!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to show all Rejected orders
@app.route('/Rejectedorders', methods=['GET'])
def show_Rejectedorders():
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Rejected_Order;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add Rejected orders
@app.route('/addRejectedorder', methods=['POST'])
def add_Rejectedorder():
    global conn
    try:
        _json = request.json
        _sr_no = _json['sr_no']
        _ISIN = _json['ISIN']
        _price = _json['price']
        _BOS = _json['BOS']
        _qty = _json['qty']
        _aon = _json['aon']
        _LOM = _json['LOM']

        if _sr_no and _ISIN and _price and _BOS and _qty and _aon and _LOM and request.method == 'POST':
            sqlQuery = "INSERT INTO rejected_order(sr_no,ISIN,price,BOS,qty,aon,LOM) VALUES(%s, %s, %s, %s, %s, %s, %s);"
            bindData = (_sr_no,_ISIN, _price, _BOS, _qty, _aon, _LOM)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Rejected Order added successfully!')
            response.status_code = 200
            return response
        else:
            return not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to show all Manual orders
@app.route('/Manualorders', methods=['GET'])
def show_Manualorders():
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  Manual_Orders;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add Rejected orders
@app.route('/addManualorder', methods=['POST'])
def add_Manualorder():
    global conn
    try:
        _json = request.json
        _ISIN = _json['ISIN']
        _price = _json['price']
        _qty = _json['qty']
        _aon = _json['aon']
        _identifier = _json['identifier']
        _BOS = _json['BOS']
        _LOM = _json['LOM']

        if _ISIN and _price and _qty and _aon and _identifier and _BOS and _LOM and request.method == 'POST':
            sqlQuery = "INSERT INTO manual_orders(ISIN,price,qty,aon,identifier,BOS,LOM) VALUES(%s, %s, %s, %s,%s,%s,%s);"
            bindData = (_ISIN, _price, _qty, _aon, _identifier, _BOS, _LOM)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Manual Order added successfully!')
            response.status_code = 200
            return response
        else:
            return not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to show all Trades
@app.route('/trade', methods=['GET'])
def show_trade():
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  Trade_Index;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add trade
@app.route('/addtrade', methods=['POST'])
def add_trade():
    global conn
    try:
        _json = request.json
        _id = _json['id']
        _buyorder_id = _json['buyorder_id']
        _sellorder_id = _json['sellorder_id']
        _price = _json['price']
        _qty = _json['qty']
        if _id and _buyorder_id and _sellorder_id and _price and _qty and request.method == 'POST':
            sqlQuery = "INSERT INTO trade_index(id,buyorder_id,sellorder_id,price,qty) VALUES(%s,%s, %s, %s, %s);"
            bindData = (_id, _buyorder_id, _sellorder_id, _price, _qty)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('trade added successfully!')
            response.status_code = 200
            return response
        else:
            return not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to show portfolio
@app.route('/portfolio', methods=['GET'])
def show_porfolio():
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  My_Portfolio;")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()


# endpoint to add to portfolio
@app.route('/addportfolio', methods=['POST'])
def add_portfolio():
    global conn
    try:
        _json = request.json
        _ISIN = _json['ISIN']
        _name = _json['name']
        _qty = _json['qty']

        if _ISIN and _name and _qty and request.method == 'POST':
            sqlQuery = "INSERT INTO my_portfolio(ISIN,name,qty) VALUES(%s,%s, %s);"
            bindData = (_ISIN, _name, _qty)
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Addition to portfolio successful!')
            response.status_code = 200
            return response
        else:
            return not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=False)


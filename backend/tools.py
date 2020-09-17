import mysql.connector
from datetime import datetime
from backend.randomOrderGenerator import q

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="oms"
)

offset = 0


def ClearOrders():
    global conn
    curr = conn.cursor()
    curr.execute('''delete from order_index;''')
    conn.commit()
    curr.execute('''delete from trade_index;''')
    conn.commit()
    curr.execute('''delete from Rejected_order;''')
    conn.commit()
    # TODO: set all quantities in my portfolio as 0
    # curr.execute('''delete from My_Portfolio''')
    # conn.commit()


def DeleteOrder(id):
    global conn
    curr = conn.cursor(prepared=True)
    curr.execute('''update order_index set identifier = ? where id = ?;''', ("1", id))
    conn.commit()


def UpdateQuantity(id, change):
    global conn
    curr = conn.cursor(prepared=True)
    curr.execute('''update order_index set qty = qty + ? where id = ?;''', (change, id))
    conn.commit()


def InsertTrade(buy, sell, quan, price):
    global conn
    cur = conn.cursor(prepared=True)
    if buy[0].startswith('m'):
        cur.execute('''update My_Portfolio set qty = qty + ? where name = ?;''', (quan, buy[1]))
        conn.commit()
    if sell[0].startswith('m'):
        cur.execute('''update My_Portfolio set qty = qty - ? where name = ?;''', (quan, sell[1]))
        conn.commit()
    cur.execute('''insert into trade_index (buyorder_id, sellorder_id, price, qty) values (?, ?, ?, ?);''',
                (buy[0], sell[0], price, quan))
    conn.commit()
    q.b -= quan
    q.s -= quan


def CreatePortfolio():
    global conn
    cur = conn.cursor()
    cur.execute('''insert into my_portfolio values('APP1984', 'Apple', 0);''')
    conn.commit()
    cur.execute('''insert into my_portfolio values('MIC1990', 'Microsoft', 0);''')
    conn.commit()
    cur.execute('''insert into my_portfolio values('IBM1950', 'IBM', 0);''')
    conn.commit()
    cur.execute('''insert into my_portfolio values('XER1960', 'Xerox', 0);''')
    conn.commit()
    cur.execute('''insert into my_portfolio values('PIX1991', 'Pixar', 0);''')
    conn.commit()


def ManualOrders(ol):
    global conn, offset, q
    cur = conn.cursor()
    cur1 = conn.cursor(prepared=True)
    cur.execute('''select * from Manual_Orders;''')
    rows = cur.fetchall()

    if len(rows) > offset:
        for i in range(offset, len(rows)):
            tempRow = rows[i + offset]
            orderID = 'm' + str(tempRow[0])

            if tempRow[7] == 'b' and q.s < tempRow[4] and tempRow[8] == 'm':
                cur1.execute(
                    '''insert into Rejected_Order (ISIN, price, BOS, qty, aon, LOM) values (?, ?, ?, ?, ?, ?);''',
                    (tempRow[2], tempRow[3], tempRow[7], tempRow[4], tempRow[5], tempRow[8]))
                conn.commit()
            elif tempRow[7] == 's' and q.b < tempRow[4] and tempRow[8] == 'm':
                cur1.execute(
                    '''insert into Rejected_Order (ISIN, price, BOS, qty, aon, LOM) values (?, ?, ?, ?, ?, ?);''',
                    (tempRow[2], tempRow[3], tempRow[7], tempRow[4], tempRow[5], tempRow[8]))
                conn.commit()
            else:
                ol.append(
                    [orderID, tempRow[1], tempRow[4], tempRow[5], tempRow[7], tempRow[8], tempRow[3], datetime.now(),
                     int(0), tempRow[2]])
                cur1.execute('''insert into order_index values(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                    orderID, tempRow[2], tempRow[3], tempRow[4], tempRow[5], 0, tempRow[7], tempRow[8], tempRow[1]))
                conn.commit()
                # SurfExcel()
    offset = len(rows)

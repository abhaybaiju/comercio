import mysql.connector
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


def InsertTrade(buyID, sellID, quan, price):
    global conn
    cur = conn.cursor(prepared=True)
    cur.execute('''insert into trade_index (buyorder_id, sellorder_id, price, qty) values (?, ?, ?, ?);''', (buyID, sellID, price, quan))
    conn.commit()
    q.b-=quan
    q.s-=quan


def HandlePortfolio(name, isin, quan):
    global conn
    cur = conn.cursor()
    cur.execute('''select name from My_Portfolio;''')
    temp = cur.fetchall()
    neo = conn.cursor(prepared=True)
    if name in temp:
        neo.execute('''update My_Portfolio set qty = qty + ? where name = ?;''', (quan, name))
    else:
        neo.execute('''insert into My_Portfolio values (?, ?, ?)''', (isin, name, quan))
    conn.commit()


def ManualOrders(ol):
    global conn, offset, q
    cur = conn.cursor()
    cur.execute('''select * from Manual_Orders;''')
    rows = cur.fetchall()
    if len(rows) > offset:
        for i in range(len(rows)):
            tempRow = rows[i+offset]
            orderID = 'm'+str(tempRow[0])
            dummy = [tempRow[1], tempRow[2], tempRow[3], tempRow[4], tempRow[5], tempRow[6], tempRow[7], tempRow[8]]
            if tempRow[4] == 'b' and q.s < tempRow[2] and tempRow[5] == 'm':
                print('rejected trade b m')
            elif tempRow[4] == 's' and q.b < tempRow[2] and tempRow[5] == 'm':
                print('rejected trade s m')
            else:
                ol.append([orderID, tempRow[1], tempRow[2], tempRow[3], tempRow[4], tempRow[5], tempRow[6], tempRow[7], tempRow[8]])
    offset=len(rows)

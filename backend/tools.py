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
    if buyID.startswith('m'):
        InsertPortfolio(buyID, quan)
    if sellID.startswith('m'):
        InsertPortfolio(sellID, quan)
    cur = conn.cursor(prepared=True)
    cur.execute('''insert into trade_index (buyorder_id, sellorder_id, price, qty) values (?, ?, ?, ?);''', (buyID, sellID, price, quan))
    conn.commit()
    q.b-=quan
    q.s-=quan


def InsertPortfolio(orderID, quan):
    global conn
    cur = conn.cursor(prepared=True)
    cur.execute('''select * from order_index where id = ?;'''(orderID))
    temp = cur.fetchall()
    neo = conn.cursor(prepared=True)
    if orderID in temp:
        neo.execute('''update My_Portfolio set qty = qty + ? where name = ?;''', (quan, temp[-1]))
    else:
        neo.execute('''insert into My_Portfolio values (?, ?, ?)''', (temp[1], temp[-1], quan))
    conn.commit()


def ManualOrders(ol):
    global conn, offset, q
    cur = conn.cursor()
    cur1 = conn.cursor(prepared=True)
    cur2 = conn.cursor(prepared=True)
    cur2.execute('''select sum(qty) from order_index where identifier=0;''')
    t1 = cur2.fetchall()
    print(str(t1[0][0]))
    q.b = t1[0][0]
    cur2.execute('''select sum(qty) from order_index where BOS="s";''')
    t2 = cur2.fetchall()
    q.s = t2[0][0]
    print(str(t2[0][0]))
    cur.execute('''select * from Manual_Orders;''')
    rows = cur.fetchall()
    print('outside stupid '+str(q.b)+' '+str(q.s))
    if len(rows) > offset:
        for i in range(offset, len(rows)):
            print('inside i***************************************************')
            tempRow = rows[i+offset]
            orderID = 'm'+str(tempRow[0])
            # dummy = [tempRow[1], tempRow[2], tempRow[3], tempRow[4], tempRow[5], tempRow[6], tempRow[7], tempRow[8]]
            if tempRow[7] == 'b' and q.s < tempRow[4] and tempRow[8] == 'm':
                print(str(q.s)+'******gygdyvdeyyevfyveyfvy')
                cur1.execute('''insert into Rejected_Order (ISIN, price, BOS, qty, aon, LOM) values (?, ?, ?, ?, ?, ?);''', (tempRow[2], tempRow[3], tempRow[7], tempRow[4], tempRow[5], tempRow[8]))
                conn.commit()
            elif tempRow[7] == 's' and q.b < tempRow[4] and tempRow[8] == 'm':
                print(str(q.b)+'******gygdyvdeyyevfyveyfvy')
                cur1.execute('''insert into Rejected_Order (ISIN, price, BOS, qty, aon, LOM) values (?, ?, ?, ?, ?, ?);''', (tempRow[2], tempRow[3], tempRow[7], tempRow[4], tempRow[5], tempRow[8]))
                conn.commit()
            else:
                ol.append([orderID, tempRow[1], tempRow[2], tempRow[3], tempRow[4], tempRow[5], tempRow[6], tempRow[7], tempRow[8]])
                cur1.execute('''insert into order_index values(?, ?, ?,?,?,?,?,?,? )''', (orderID, tempRow[2], tempRow[3], tempRow[4], tempRow[5], 0, tempRow[7], tempRow[8], tempRow[1]))

    offset=len(rows)

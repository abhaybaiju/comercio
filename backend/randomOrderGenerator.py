import random
from datetime import datetime
import mysql.connector
from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice, CreateEquityList, GetISIN


class Quantity:
    def __init__(self, x=0, y=0):
        self.b = x
        self.s = y


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="oms"
)

index = 0
# variable that locks off any changes to the index during random order generation
indexLocked = bool(0)

q = Quantity(0, 0)

CreateEquityList()


def RandomGenerator(num):
    numberOfOrders = num
    global index, indexLocked, conn, q
    ordersList = []

    # locking the index
    indexLocked = 1

    for i in range(0, numberOfOrders):
        index += 1
        orderID = str(index)
        orderName = equityNames[random.randint(0, (len(equityNames) - 1))]
        orderQuantity = random.randint(1, 200)
        orderAON = bool(random.getrandbits(1))
        orderBOS = bool(random.getrandbits(1))
        orderISIN = GetISIN(orderName)
        if (random.getrandbits(1)):
            orderPrice = GetRandomPrice(orderName)
            orderLOM = 'l'
        else:
            orderPrice = 0
            orderLOM = 'm'

        cur = conn.cursor(prepared=True)
        if orderBOS == 0:
            ordersList.append(
                [orderID, orderName, orderQuantity, orderAON, 'b', orderLOM, orderPrice, datetime.now(), int(0),
                 orderISIN])
            cur.execute('''INSERT INTO Order_Index values(?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                        (orderID, orderISIN, orderPrice, orderQuantity, orderAON, 0, 'b', orderLOM, orderName))
            conn.commit()
        else:
            ordersList.append(
                [orderID, orderName, orderQuantity, orderAON, 's', orderLOM, orderPrice, datetime.now(), int(0),
                 orderISIN])
            cur.execute('''INSERT INTO Order_Index values(?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                        (orderID, orderISIN, orderPrice, orderQuantity, orderAON, 0, 's', orderLOM, orderName))
            conn.commit()

        if orderBOS == '0':
            q.b += orderQuantity
        else:
            q.s += orderQuantity

        UpdateBatchSize(orderName)

    indexLocked = 0
    return ordersList

import random
from datetime import datetime
import mysql.connector

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice, CreateEquityList, GetISIN
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="oms"
)

index = 0
# variable that locks off any changes to the index during random order generation
indexLocked = bool(0)


class Quantity:
    def __init__(self, x=0, y=0):
        self.b = x
        self.s = y
q = Quantity(0, 0)

CreateEquityList()


def RandomGenerator(num):
    numberOfOrders = num
    global index, indexLocked, ordersDf, eq, conn, q
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
                [orderID, orderName, orderQuantity, orderAON, 'b', orderLOM, orderPrice, datetime.now(), int(0), orderISIN])

        else:
            ordersList.append(
                [orderID, orderName, orderQuantity, orderAON, 's', orderLOM, orderPrice, datetime.now(), int(0), orderISIN])
        cur.execute('''INSERT INTO Order_Index values(?, ?, ?, ?, ?, ?, ?, ?);''',
                    (orderID, orderISIN, orderPrice, orderQuantity, orderAON, 0, orderBOS, orderLOM))
        if orderBOS == 'b':
            q.b+=orderQuantity
        else:
            q.s+=orderQuantity
        conn.commit()
        UpdateBatchSize(orderName)


    indexLocked = 0
    return ordersList


if __name__ == '__main__':
    print('main rog')

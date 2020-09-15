import random
from datetime import datetime

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice, CreateEquityList

index = 0
# variable that locks off any changes to the index during random order generation
indexLocked = bool(0)

ordersList = list()
CreateEquityList()

def RandomGenerator(num):
    numberOfOrders = num
    global index, indexLocked, buyOrdersList, sellOrdersList, ordersDf, eq
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
        if (random.getrandbits(1)):
            orderPrice = GetRandomPrice(orderName)
            orderLOM = 'l'
        else:
            orderPrice = 0
            orderLOM = 'm'

        if orderBOS == 0:
            ordersList.append(
                [orderID, orderName, orderQuantity, orderAON, 'b', orderLOM, orderPrice, datetime.now(), int(0)])
        else:
            ordersList.append(
                [orderID, orderName, orderQuantity, orderAON, 's', orderLOM, orderPrice, datetime.now(), int(0)])
        UpdateBatchSize(orderName)

    indexLocked = 0
    return ordersList


if __name__ == '__main__':
    print('main rog')

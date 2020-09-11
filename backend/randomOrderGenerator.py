from datetime import datetime
import random
from backend.securityGenerator import equity, equityNames, equityList, GetEquityAttributes, UpdateBatchSize, GetRandomPrice
# default ISIN index
index = 100000000
indexLocked = bool(0)

buyOrdersList = list()
sellOrdersList = list()

# the price doubles up as the market/limit order indicator
# if the price is 0, the order is a market order, else it is a limit order
# the buyOrSell variable, 0 is buy, 1 is sell
class order:
    def __init__(self, id, name, quantity, allOrNothing, buyOrSell, price):
        self.id = int(id)
        self.name = str(name)
        self.quantity = int(quantity)
        self.allOrNothing = bool(allOrNothing)
        self.buyOrSell = bool(buyOrSell)
        self.price = int(price)
        self.stamp = str(datetime.now())

def RandomGenerator(self, minOrders = 50 , maxOrders = 100):
    if minOrders > maxOrders:
        t = minOrders
        minOrders = maxOrders
        maxOrders = t
    elif minOrders == maxOrders:
        minOrders = 50
        maxOrders = 100

    global index, indexLocked, buyOrdersList, sellOrdersList
    indexLocked = 1

    for i in range(minOrders, maxOrders):
        index+=1
        orderID = index
        orderName = equityNames[random.randint(0, (len(equityNames) - 1))]
        orderQuantity = random.randint(1, 200)
        orderAON = bool(random.getrandbits(1))
        orderBOS = bool(random.getrandbits(1))
        if(random.getrandbits(1)):
            orderPrice = GetRandomPrice(orderName)
        else:
            orderPrice = 0

        if(orderBOS == 0):
            buyOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
        else:
            sellOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
        UpdateBatchSize(orderName)

RandomGenerator(100, 200)
print(len(buyOrdersList))
print(len(sellOrdersList))



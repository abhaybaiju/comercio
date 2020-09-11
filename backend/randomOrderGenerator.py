import random
from datetime import datetime

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice

# default ISIN index
# for each new day the order would be X00000000 where X is the number of the day
index = 100000000
# variable that locks off any changes to the index during random order generation
indexLocked = bool(0)

# separate lists that contain order objects
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

    # returns the atttributes of the order as a list
    def RetrieveOrderAttributes(self):
        resultList = list()
        resultList.extend(
            [self.id, self.name, self.quantity, self.allOrNothing, self.buyOrSell, self.price, self.stamp])
        return resultList


# the random order generator, default arguments are
def RandomGenerator(self, minOrders=50, maxOrders=100):
    if minOrders > maxOrders:
        t = minOrders
        minOrders = maxOrders
        maxOrders = t
    elif minOrders == maxOrders:
        minOrders = 50
        maxOrders = 100

    numberOfOrders = random.randint(minOrders, maxOrders)

    global index, indexLocked, buyOrdersList, sellOrdersList

    # locking the index
    indexLocked = 1

    for i in range(0, numberOfOrders):
        index += 1
        orderID = index
        orderName = equityNames[random.randint(0, (len(equityNames) - 1))]
        orderQuantity = random.randint(1, 200)
        orderAON = bool(random.getrandbits(1))
        orderBOS = bool(random.getrandbits(1))
        if (random.getrandbits(1)):
            orderPrice = GetRandomPrice(orderName)
        else:
            orderPrice = 0

        if (orderBOS == 0):
            buyOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
        else:
            sellOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
        UpdateBatchSize(orderName)

    indexLocked = 0


RandomGenerator(100, 200)
print(len(buyOrdersList))
print(len(sellOrdersList))


# prints the order details from the two order list
# argument 0 is for the buy list and 1 for the sell list
def PrintOrderDetails(x):
    global buyOrdersList, sellOrdersList

    if x == 0:
        print('Printing the buy orders:')
        for i in buyOrdersList:
            result = i.RetrieveOrderAttributes()
            print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + ' ' + str(result[3]) + ' ' + str(
                result[4]) + ' ' + str(result[5]) + ' ' + str(result[6]))
    else:
        print('Printing the sell orders:')
        for i in sellOrdersList:
            result = i.RetrieveOrderAttributes()
            print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + ' ' + str(result[3]) + ' ' + str(
                result[4]) + ' ' + str(result[5]) + ' ' + str(result[6]))


PrintOrderDetails(0)
PrintOrderDetails(1)

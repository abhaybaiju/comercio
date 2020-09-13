import random
from datetime import datetime

import pandas as pd

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice

# default ISIN index
# for each new day the order would be X00000000 where X is the number of the day
index = 0
# variable that locks off any changes to the index during random order generation
indexLocked = bool(0)

# separate lists that contain order objects
# buyOrdersList = list()
# sellOrdersList = list()

# buyDf = pd.DataFrame(columns=['id', 'name', 'AON', 'BOS', 'price', 'stamp'])
# buyDf = pd.DataFrame()
# sellDf = pd.DataFrame()
ordersDf = pd.DataFrame()
ordersList = list()

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

    def PrintOrder(self):
        result = list()
        result.extend(
            [self.id, self.name, self.quantity, self.allOrNothing, self.buyOrSell, self.price, self.stamp])
        print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + ' ' + str(result[3]) + ' ' + str(
            result[4]) + ' ' + str(result[5]) + ' ' + str(result[6]))


# the random order generator, default arguments are
def RandomGenerator(self, minOrders=50, maxOrders=100):
    if minOrders > maxOrders:
        t = minOrders
        minOrders = maxOrders
        maxOrders = t
    elif minOrders == maxOrders:
        minOrders = 50
        maxOrders = 100

    # numberOfOrders = random.randint(minOrders, maxOrders)
    numberOfOrders = 100
    global index, indexLocked, buyOrdersList, sellOrdersList, ordersDf, ordersList

    # locking the index
    indexLocked = 1

    for i in range(0, numberOfOrders):
        index += 1
        orderID = str(index)
        orderName = equityNames[random.randint(0, (len(equityNames) - 1))]
        # orderName = 'Microsoft'
        # orderQuantity = random.randint(1, 200)
        orderQuantity = random.choice([100, 200])
        orderAON = bool(random.getrandbits(1))
        orderBOS = bool(random.getrandbits(1))
        if (random.getrandbits(1)):
            orderPrice = GetRandomPrice(orderName)
            orderLOM = 'l'
        else:
            orderPrice = 0
            orderLOM = 'm'

        if (orderBOS == 0):
            # buyOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
            temp = pd.Series([orderID, orderName, orderQuantity, orderAON, 'b', orderLOM, orderPrice, datetime.now(), 0])
            # print(temp)
            # buyDf = buyDf.append(temp, ignore_index=True)
            # ordersDf = ordersDf.append(temp, ignore_index=True)
            ordersList.append([orderID, orderName, orderQuantity, orderAON, 'b', orderLOM, orderPrice, datetime.now(), 0])
            # print('*****')
        else:
            # sellOrdersList.append(order(orderID, orderName, orderQuantity, orderAON, orderBOS, orderPrice))
            temp = pd.Series([orderID, orderName, orderQuantity, orderAON, 's', orderLOM, orderPrice, datetime.now(), 0])
            # print(temp)
            # sellDf = sellDf.append(temp, ignore_index=True)
            # ordersDf = ordersDf.append(temp, ignore_index=True)
            ordersList.append([orderID, orderName, orderQuantity, orderAON, 's', orderLOM, orderPrice, datetime.now(), 0])
            # print('*****')
        UpdateBatchSize(orderName)

    indexLocked = 0
    # ordersDf.columns = ['id', 'name', 'quantity', 'AON', 'BOS', 'LOM', 'price', 'timestamp', 'done']
    return ordersList


# prints the order details from the two order list
# argument 0 is for the buy list and 1 for the sell list
def PrintOrderDetails():
    global buyOrdersList, sellOrdersList, buyDf, sellDf, ordersDf

    # if x == 0:
    #     print('Printing the buy orders:')
    #     # for i in buyOrdersList:
    #     #     result = i.RetrieveOrderAttributes()
    #     #     print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + ' ' + str(result[3]) + ' ' + str(
    #     #         result[4]) + ' ' + str(result[5]) + ' ' + str(result[6]))
    #     print(buyDf)
    #     print('*****')
    # else:
    #     print('Printing the sell orders:')
    #     # for i in sellOrdersList:
    #     #     result = i.RetrieveOrderAttributes()
    #     #     print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + ' ' + str(result[3]) + ' ' + str(
    #     #         result[4]) + ' ' + str(result[5]) + ' ' + str(result[6]))
    #     print(sellDf)
    #     print('*****')
    print(ordersDf)
    print('*****')

def RetrieveSorted(buyOrSell):
    global ordersDf
    # 0 is for buy order, 1 is for sell order
    if buyOrSell == 0:
        # tempDf = (ordersDf.loc[(ordersDf[4].isin(['s'])) & (ordersDf[5].isin(['l']))])
        tempDf = ordersDf[(ordersDf.BOS == 's') & (ordersDf.LOM == 'l')]
        tempDf = tempDf.sort_values(by=['price'], ascending=True)
        return tempDf
    elif buyOrSell == 1:
        # tempDf = (ordersDf.loc[(ordersDf[4].isin(['b'])) & (ordersDf[5].isin(['l']))])
        tempDf = ordersDf[(ordersDf.BOS == 's') & (ordersDf.LOM == 'l')]
        tempDf = tempDf.sort_values(by=['price'], ascending=False)
        return tempDf

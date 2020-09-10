import random

# the equities list is a predefined list of the names of all the different stocks/companies
equityNames = list(('Apple', 'Microsoft', 'IBM', 'Xerox', 'Pixar'))


# the equities class
class equity:
    # constructor for the equity objects
    def __init__(self, name, price, batchSize, trend):
        self.name = name
        self.price = price
        self.batchSize = batchSize
        self.trend = bool(trend)

    def PrintAtrributes(self):
        print(self.name + ' ' + self.price + ' ' + self.batchSize + ' ' + self.trend)

    # to be called when a transaction is performed to update the spot price
    def UpdatePrice(self, newPrice):
        self.price = newPrice

    # function to be called when a new order is generated
    # decreases the remaining batch size
    # when batch depleted generates a pseudorandom batch size and randomly changes the trend
    def DecrementBatchSize(self):
        if self.batchSize > 1:
            self.batchSize = self.batchSize - 1
        else:
            self.batchSize = random.randint(3, 10)
            self.trend = random.getrandbits(1)


# creating the list of the equity objects
equityList = list()
equityList.append(equity('Apple', 700, 5, 1))
equityList.append(equity('Microsoft', 500, 4, 1))
equityList.append(equity('IBM', 350, 5, 0))
equityList.append(equity('Xerox', 200, 3, 0))
equityList.append(equity('Pixar', 550, 7, 1))


# function to retrieve the attributes of a particular equity
def GetEquityAttributes(find):
    resultlist = list()
    for i in equityList:
        if i.name == find:
            resultlist.append(i.price)
            resultlist.append(i.batchSize)
            resultlist.append(i.trend)
            return resultlist


# function to decrement the batch size of the equity when a new order is generated
def UpdateBatchSize(find):
    for i in equityList:
        if i.name == find:
            i.DecrementBatchSize()
            break


# function to update equity price when trade occurs
def UpdateEquityPrice(find, newPrice):
    for i in equityList:
        if i.name == find:
            i.UpdatePrice(newPrice)
            break

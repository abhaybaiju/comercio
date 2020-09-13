import random
from datetime import datetime

import pandas as pd
import time

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice
from backend.randomOrderGenerator import index, indexLocked, RandomGenerator, PrintOrderDetails, RetrieveSorted
ordersList = []
ordersList = RandomGenerator(100, 200)
print(ordersList)

def Match():
    print('Length of '+str(len(ordersList)))
    count = 0
    flagged = 0
    iC = 0
    for i in ordersList:
        if i[8] == 0:
            if i[4] == 's' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 'b' and j[8] == 0:
                        if j[6] >= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] = 1
                                ordersList[iC][8] = 1
                                iC = iC+1
                                count=count+1
            elif i[4] == 'b' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 's' and j[8] == 0:
                        if j[6] <= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] = 1
                                ordersList[iC][8] = 1
                                iC = iC+1
                                count=count+1
    print(str(count) + ' Transactions')
    for i in ordersList:
        if i[8] == 1:
            flagged=flagged+1
    print(str(flagged)+' were found')


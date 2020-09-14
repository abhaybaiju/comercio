from operator import itemgetter
import random
from datetime import datetime

import pandas as pd
import time

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice
from backend.randomOrderGenerator import index, indexLocked, RandomGenerator, PrintOrderDetails, RetrieveSorted

ordersList = []
ordersList = RandomGenerator(100, 200)


def Match():
    global ordersList
    iC = 0
    doneOrders = []

    for i in ordersList:
        if ordersList[iC][8] == 0:
            # s l
            if i[4] == 's' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 'b' and ordersList[ReturnJC(j[0])][8] == 0 and j[5] == 'l':
                        if j[6] >= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(i[2]))
                                print('i < j')
                            break
            # b l
            elif i[4] == 'b' and i[5] == 'l':
                tempQ = i[2]
                for j in ordersList:
                    if j[4] == 's' and ordersList[ReturnJC(j[0])][8] == 0 and j[5] == 'l':
                        if j[6] <= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(i[2]))
                                print(str(tempQ) + '***')
                                print('i < j')
                            break
            # s m
            if i[4] == 's' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(filter(lambda x: x[4] == 's' and x[1] == i[1], ordersList), 6, False)
                for j in tempList:
                    jC = ReturnJC(j[0])
                    if ordersList[jC][8] == 0 and j[4] == 'b' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            print('j > i')
                            tempQ = tempQ - j[2]
                            print(str(tempQ) + '*****')
                        if (tempQ == 0):
                            break
            # b m
            if i[4] == 'b' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(filter(lambda x: x[4] == 's' and x[1] == i[1], ordersList), 6, False)
                for j in tempList:
                    jC = ReturnJC(j[0])
                    if ordersList[jC][8] == 0 and j[4] == 's' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            print('j > i')
                            tempQ = tempQ - j[2]
                            print(str(tempQ) + '*****')
                        if (tempQ == 0):
                            break
        iC = iC + 1

    for i in ordersList:
        print(i[8])


def SortList(ordersL, indexOfList, reverseOrNot):
    res = sorted(ordersL, key=itemgetter(indexOfList), reverse=reverseOrNot)
    return res


def ReturnJC(jID):
    global ordersList
    counter = 0
    for x in ordersList:
        if x[0] == jID:
            return counter
        else:
            counter = counter + 1


Match()

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
    marker = list()
    for i in range(0, len(ordersList)):
        marker.append(0)

    for i in ordersList:
        if marker[iC] == 0:
            # s l
            if i[4] == 's' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 'b' and marker[ReturnJC(ordersList, j[0])] == 0 and j[5] == 'l':
                        if j[6] >= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                marker[iC] += 1
                                jC = ReturnJC(ordersList, j[0])
                                marker[jC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                marker[jC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                marker[iC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(i[2]))
                                print('i < j')
                            break
            # b l
            elif i[4] == 'b' and i[5] == 'l':
                tempQ = i[2]
                for j in ordersList:
                    if j[4] == 's' and marker[ReturnJC(ordersList, j[0])] == 0 and j[5] == 'l':
                        if j[6] <= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                marker[iC] += 1
                                jC = ReturnJC(ordersList, j[0])
                                marker[jC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                marker[jC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                marker[iC] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(i[2]))
                                print(str(tempQ)+'***')
                                print('i < j')
                            break
            # s m
            elif i[4] == 's' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(ordersList, 6, True)
                for j in tempList:
                    jC = ReturnJC(ordersList, j[0])
                    if marker[jC] == 0 and j[4] == 'b':
                        if tempQ == j[2]:
                            marker[iC] += 1
                            jC = ReturnJC(ordersList, j[0])
                            marker[jC] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            marker[iC] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            marker[jC] += 1
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            print('j > i')
                            tempQ = tempQ - j[2]
                            print(str(tempQ)+'*****')
                        if(tempQ == 0):
                            break
            # b m
            elif i[4] == 'b' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(ordersList, 6, False)
                for j in tempList:
                    jC = ReturnJC(ordersList, j[0])
                    if marker[jC] == 0 and j[4] == 's':
                        if tempQ == j[2]:
                            marker[iC] += 1
                            jC = ReturnJC(ordersList, j[0])
                            marker[jC] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            marker[iC] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            marker[jC] += 1
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            print('j > i')
                            tempQ = tempQ - j[2]
                            print(str(tempQ)+'*****')
                        if(tempQ == 0):
                            break
        iC = iC + 1

    for i in marker:
        print(i)

    # print(str(count) + ' Transactions')
    # flagged = 0
    # for i in marker:
    #     if i == 1:
    #         flagged = flagged + 1
    # print(str(flagged) + ' were found')


def SortList(inputList, indexOfList, reverseOrNot):
    res = sorted(inputList, key=itemgetter(indexOfList), reverse=reverseOrNot)
    return res


def ReturnJC(inputList, jID):
    counter = 0
    for x in inputList:
        if x[0] == jID:
            return counter
        else:
            counter = counter + 1


def Delete(iC, jC):
    global ordersList


Match()

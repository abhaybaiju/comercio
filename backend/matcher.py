import mysql.connector
from operator import itemgetter
from backend.randomOrderGenerator import RandomGenerator
from backend.tools import DeleteOrder, UpdateQuantity, ManualOrders, ClearOrders, InsertTrade

ordersList = RandomGenerator(100)
doneOrders = []

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="oms"
)


def Match():
    ClearOrders()
    global ordersList, doneOrders, conn
    iC = 0
    doneOrders = []
    last = -1
    cur = conn.cursor(prepared=True)

    while True:
        i = ordersList[iC]
        if ordersList[iC][8] == 0:
            # s l
            if i[4] == 's' and i[5] == 'l' and i[8] == 0:
                tempQ = i[2]
                for j in filter(lambda x:x[8] != 1, ordersList):
                    if j[4] == 'b' and ordersList[ReturnJC(ordersList, j[0])][8] == 0 and j[5] == 'l':
                        if j[6] >= i[6] and i[1] == j[1]:
                            if tempQ == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[jC], ordersList[iC], tempQ, j[6])
                                DeleteOrder(ordersList[iC][0])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = 0
                            elif tempQ > j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[jC], ordersList[iC], j[2], j[6])
                                ordersList[iC][2] = (int(tempQ) - int(j[2]))
                                UpdateQuantity(ordersList[iC][0], j[2])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = tempQ - j[2]
                            elif tempQ < j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[jC], ordersList[iC], tempQ, j[6])
                                ordersList[jC][2] = (int(j[2]) - int(tempQ))
                                UpdateQuantity(ordersList[jC][0], i[2])
                                DeleteOrder(ordersList[iC][0])
                                tempQ = 0
                            if tempQ == 0:
                                break
            # b l
            elif i[4] == 'b' and i[5] == 'l' and i[8] == 0:
                for j in ordersList:
                    if j[4] == 's' and ordersList[ReturnJC(ordersList, j[0])][7] == 0 and j[5] == 'l':
                        if j[6] <= i[6] and i[1] == j[1]:
                            tempQ = i[2]
                            if tempQ == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[iC], ordersList[jC], tempQ, j[6])
                                DeleteOrder(ordersList[iC][0])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = 0
                            elif tempQ > j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[iC], ordersList[jC], j[2], j[6])
                                ordersList[iC][2] = (int(tempQ) - int(j[2]))
                                UpdateQuantity(ordersList[iC][0], j[2])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = tempQ - j[2]
                            elif tempQ < j[2]:
                                jC = ReturnJC(ordersList, j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                InsertTrade(ordersList[iC], ordersList[jC], tempQ, j[6])
                                ordersList[jC][2] = (int(j[2]) - int(tempQ))
                                UpdateQuantity(ordersList[jC][0], i[2])
                                DeleteOrder(ordersList[iC][0])
                                tempQ = 0
                            if tempQ == 0:
                                break
            # s m
            if i[4] == 's' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(filter(lambda x: x[4] == 'b' and x[1] == i[1] and x[5] == 'l', ordersList), 6, True)
                for j in tempList:
                    jC = ReturnJC(ordersList, j[0])
                    if ordersList[jC][8] == 0 and j[4] == 'b' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[jC], ordersList[iC], j[2], j[6])
                            DeleteOrder(ordersList[iC][0])
                            DeleteOrder(ordersList[jC][0])
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[jC], ordersList[iC], tempQ, j[6])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            UpdateQuantity(ordersList[jC][0], tempQ)
                            DeleteOrder(ordersList[iC][0])
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[jC], ordersList[iC], j[2], j[6])
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            tempQ = tempQ - j[2]
                            UpdateQuantity(ordersList[iC][0], j[2])
                            DeleteOrder(ordersList[jC][0])
                        if tempQ == 0:
                            break
            # b m
            if i[4] == 'b' and i[5] == 'm':
                tempQ = i[2]
                tempList = SortList(filter(lambda x: x[4] == 's' and x[1] == i[1] and x[5] == 'l', ordersList), 6, False)
                for j in tempList:
                    jC = ReturnJC(ordersList, j[0])
                    if ordersList[jC][8] == 0 and j[4] == 's' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[iC], ordersList[jC], tempQ, j[6])
                            DeleteOrder(ordersList[iC][0])
                            DeleteOrder(ordersList[jC][0])
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[iC], ordersList[jC], tempQ, j[6])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            UpdateQuantity(ordersList[jC][0], tempQ)
                            DeleteOrder(ordersList[iC][0])
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(ordersList, j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            InsertTrade(ordersList[iC], ordersList[jC], j[2], j[6])
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            tempQ = tempQ - j[2]
                            UpdateQuantity(ordersList[iC][0], j[2])
                            DeleteOrder(ordersList[jC][0])
                        if tempQ == 0:
                            break

        iC = iC + 1


        if (iC + 1) % 10 == 0:
            newRows = RandomGenerator(10)
            ordersList.extend(newRows)
            ManualOrders(ordersList)


def SortList(ordersL, indexOfList, reverseOrNot):
    res = sorted(ordersL, key=itemgetter(indexOfList), reverse=reverseOrNot)
    return res


def ReturnJC(li, jID):
    counter = 0
    for x in li:
        if x[0] == jID:
            return counter
        else:
            counter = counter + 1

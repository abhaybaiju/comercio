from operator import itemgetter
from backend.randomOrderGenerator import RandomGenerator
import mysql.connector
from backend.tools import DeleteOrder, UpdateQuantity, ManualOrders, ClearOrders
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
            if i[4] == 's' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 'b' and ordersList[ReturnJC(j[0])][8] == 0 and j[5] == 'l':
                        if j[6] >= i[6] and i[1] == j[1]:
                            tempQ = i[2]
                            if tempQ == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                DeleteOrder(ordersList[iC][0])
                                DeleteOrder(ordersList[jC][0])
                                print('i = j')
                                tempQ = 0
                            elif tempQ > j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(tempQ) - int(j[2]))
                                UpdateQuantity(ordersList[iC][0], j[2])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = tempQ - j[2]
                                print('j > i')
                            elif tempQ < j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(tempQ))
                                UpdateQuantity(ordersList[jC][0], i[2])
                                DeleteOrder(ordersList[iC][0])
                                tempQ = 0
                                print('i < j')
                            if tempQ == 0:
                                break
            # b l
            elif i[4] == 'b' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 's' and ordersList[ReturnJC(j[0])][8] == 0 and j[5] == 'l':
                        if j[6] <= i[6] and i[1] == j[1]:
                            tempQ = i[2]
                            if tempQ == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                DeleteOrder(ordersList[iC][0])
                                DeleteOrder(ordersList[jC][0])
                                print('i = j')
                                tempQ = 0
                            elif tempQ > j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(tempQ) - int(j[2]))
                                UpdateQuantity(ordersList[iC][0], j[2])
                                DeleteOrder(ordersList[jC][0])
                                tempQ = tempQ - j[2]
                                print('j > i')
                            elif tempQ < j[2]:
                                jC = ReturnJC(j[0])
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(tempQ))
                                UpdateQuantity(ordersList[jC][0], i[2])
                                DeleteOrder(ordersList[iC][0])
                                tempQ = 0
                                print('i < j')
                            if tempQ == 0:
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
                            DeleteOrder(ordersList[iC][0])
                            DeleteOrder(ordersList[jC][0])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            UpdateQuantity(ordersList[jC][0], tempQ)
                            DeleteOrder(ordersList[iC][0])
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            tempQ = tempQ - j[2]
                            UpdateQuantity(ordersList[iC][0], j[2])
                            DeleteOrder(ordersList[jC][0])
                            print('j > i')
                        if tempQ == 0:
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
                            DeleteOrder(ordersList[iC][0])
                            DeleteOrder(ordersList[jC][0])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            UpdateQuantity(ordersList[jC][0], tempQ)
                            DeleteOrder(ordersList[iC][0])
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0])
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            tempQ = tempQ - j[2]
                            UpdateQuantity(ordersList[iC][0], j[2])
                            DeleteOrder(ordersList[jC][0])
                            print('j > i')
                        if tempQ == 0:
                            break
        iC = iC + 1

        flag = 0

        for t in doneOrders:
            for t1 in t:
                if i[0] == t1:
                    flag = 1
                    break

        if flag == 0:
            last = i[0]

        if (iC + 1) % 50 == 0:
            ordersList = list(filter(lambda x: x[8] != 1, ordersList))
            newRows = RandomGenerator(10)
            ordersList.extend(newRows)
            if last != -1:
                iC = ReturnJC(last) - 1
            else:
                iC = -1
            ManualOrders(ordersList)


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

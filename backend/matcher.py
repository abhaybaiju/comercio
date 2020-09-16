from operator import itemgetter
from backend.randomOrderGenerator import RandomGenerator
import mysql.connector
ordersList = RandomGenerator(100)
doneOrders = []

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="oms"
)

def Match():
    global ordersList, doneOrders, conn
    # cur = conn.cursor(prepared=True)
    # cur.execute('''INSERT INTO Securities_Index values(?, ?, ?, ?);''', ('ffff', 'gpog', 'Stock', 666))
    # conn.commit()
    iC = 0
    doneOrders = []
    index = -1
    last = -1
    while True:
        index += 1
        i = ordersList[index]
        if ordersList[iC][8] == 0:
            # s l
            if i[4] == 's' and i[5] == 'l':
                for j in ordersList:
                    if j[4] == 'b' and ordersList[ReturnJC(j[0], ordersList)][8] == 0 and j[5] == 'l':
                        if j[6] >= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0], ordersList)
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(j[0], ordersList)
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(j[0], ordersList)
                                ordersList[iC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[jC][2] = (int(j[2]) - int(i[2]))
                                print('i < j')
                            break
            # b l
            elif i[4] == 'b' and i[5] == 'l':
                tempQ = i[2]
                for j in ordersList:
                    if j[4] == 's' and ordersList[ReturnJC(j[0], ordersList)][8] == 0 and j[5] == 'l':
                        if j[6] <= i[6] and i[1] == j[1]:
                            if i[2] == j[2]:
                                ordersList[iC][8] += 1
                                jC = ReturnJC(j[0], ordersList)
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                doneOrders.append(['***'])
                                print('i = j')
                            elif i[2] > j[2]:
                                jC = ReturnJC(j[0], ordersList)
                                ordersList[jC][8] += 1
                                doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                                ordersList[iC][2] = (int(i[2]) - int(j[2]))
                                print('j > i')
                            elif i[2] < j[2]:
                                jC = ReturnJC(j[0], ordersList)
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
                    jC = ReturnJC(j[0], ordersList)
                    if ordersList[jC][8] == 0 and j[4] == 'b' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(j[0], ordersList)
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0], ordersList)
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0], ordersList)
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
                    jC = ReturnJC(j[0], ordersList)
                    if ordersList[jC][8] == 0 and j[4] == 's' and i[1] == j[1]:
                        if tempQ == j[2]:
                            ordersList[iC][8] += 1
                            jC = ReturnJC(j[0], ordersList)
                            ordersList[jC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            doneOrders.append(['***'])
                            print('i = j')
                            tempQ = 0
                        elif tempQ < j[2]:
                            jC = ReturnJC(j[0], ordersList)
                            ordersList[iC][8] += 1
                            doneOrders.append([ordersList[iC][0], ordersList[jC][0]])
                            ordersList[jC][2] = (int(j[2]) - int(i[2]))
                            print('i < j')
                            tempQ = 0
                        elif tempQ > j[2]:
                            jC = ReturnJC(j[0], ordersList)
                            ordersList[jC][8] += 1
                            ordersList[iC][2] = (int(i[2]) - int(j[2]))
                            print('j > i')
                            tempQ = tempQ - j[2]
                            print(str(tempQ) + '*****')
                        if (tempQ == 0):
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

        if (index + 1) % 10 == 0:
            ordersList = list(filter(lambda x: x[8] != 1, ordersList))
            newRows = RandomGenerator(10)
            ordersList.extend(newRows)
            if last != -1:
                index = ReturnJC(last, ordersList) - 1
            else:
                index = -1


def SortList(ordersL, indexOfList, reverseOrNot):
    res = sorted(ordersL, key=itemgetter(indexOfList), reverse=reverseOrNot)
    return res


def ReturnJC(jID, ordersList):
    counter = 0
    for x in ordersList:
        if x[0] == jID:
            return counter
        else:
            counter = counter + 1


# Match()

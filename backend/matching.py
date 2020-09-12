import random
from datetime import datetime

import pandas as pd

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice
from backend.randomOrderGenerator import index, indexLocked, RandomGenerator, PrintOrderDetails, RetrieveSorted

# ordersDf = RandomGenerator(100, 200)

def OrderMatching():
    ordersDf = RandomGenerator(100, 200)
    # print('look at this')
    # print(ordersDf[ordersDf.LOM == 'l'])
    # print('*****')'
    for srno, i in ordersDf.iterrows():
        if (i.iloc[4] == 's' and i.iloc[5] == 'l'):
            loop = True
            for sr, j in ordersDf[ordersDf.BOS != 's'].iterrows():
                if loop == False:
                    break
                elif j.iloc[6] >= i.iloc[6] and i.iloc[1] == j.iloc[1]:
                    if i.iloc[2] == j.iloc[2]:
                        print('before')
                        print(len(ordersDf.index))
                        # ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                        ordersDf = ordersDf[ordersDf.id != str(i.iloc[0])]
                        print('after i')
                        print(len(ordersDf.index))
                        ordersDf = ordersDf[ordersDf.id != str(j.iloc[0])]
                        print('after j')
                        print(len(ordersDf.index))
                        print('s l order executed')
                        loop = False
                        break
        if (i.iloc[4] == 's' and i.iloc[5] == 'm'):
            loop = True
            tempDf = RetrieveSorted(0)
            for sr, j in tempDf.iterrows():
                if loop == False:
                    break
                if (str(i.iloc[2]) == str(j.iloc[2])) and (str(i.iloc[1]) == str(j.iloc[1])):
                    ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                    print('s m executed')
                    loop = False
                    break
        if (i.iloc[4] == 'b' and i.iloc[5] == 'l'):
            loop = True
            for sr, j in ordersDf[ordersDf.BOS != 'b'].iterrows():
                if loop == False:
                    break
                if j.iloc[6] <= i.iloc[6] and i.iloc[1] == j.iloc[1]:
                    if i.iloc[2] == j.iloc[2]:
                        ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                        print('b l order executed')
                        loop = False
                        break
        if (i.iloc[4] == 'b' and i.iloc[5] == 'm'):
            tempDf = RetrieveSorted(1)
            loop = True
            for sr, j in tempDf.iterrows():
                if loop == False:
                    break
                if (str(i.iloc[2]) == str(j.iloc[2])) and (str(i.iloc[1]) == str(j.iloc[1])):
                    ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                    print('b m executed')
                    loop = False
                    break

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
    # print('*****')
    for srno, i in ordersDf.iterrows():
        if (i.iloc[4] == 's' and i.iloc[5] == 'l'):
            for sr, j in ordersDf[ordersDf.BOS != 's'].iterrows():
                if j.iloc[6] >= i.iloc[6] and i.iloc[1] == j.iloc[1]:
                    if i.iloc[2] == j.iloc[2]:
                        ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                        print('s l order executed')
        # if (i.iloc[4] == 's' and i.iloc[5] == 'm'):
        #     tempDf = RetrieveSorted(0)
        #     for sr, j in tempDf.iterrows():
        #             if i.iloc[2] == j.iloc[2]:
        #                 ordersDf = ordersDf.drop(ordersDf.id == [i.iloc[0], j.iloc[0]].index, inplace=True)
        #                 # print('trade executed')
        #                 # print('buy order:')
        #                 # print(i)
        #                 # print('sell order:')
        #                 # print(j)
        # if i.iloc[4] == 'b' and i.iloc[5] == 'l':
        #     for sr, j in ordersDf.loc[(ordersDf[4].isin(['s']))].iterrows():
        #         if j.iloc[6] <= i.iloc[6]:
        #             if i.iloc[2] == j.iloc[2]:
        #                 ordersDf = ordersDf.drop(ordersDf.id == [i.iloc[0], j.iloc[0]].index, inplace=True)
        #                 # print('trade executed')
        #                 # print('buy order:')
        #                 # print(j)
        #                 # print('sell order:')
        #                 # print(i)
        # if i.iloc[4] == 'b' and i.iloc[5] == 'm':
        #     tempDf = RetrieveSorted(1)
        #     for sr, j in tempDf.iterrows():
        #         if j.iloc[6] <= i.iloc[6]:
        #             if i.iloc[2] == j.iloc[2]:
        #                 ordersDf = ordersDf.drop(ordersDf.id == [i.iloc[0], j.iloc[0]].index, inplace=True)
        #                 # print('trade executed')
        #                 # print('buy order:')
        #                 # print(i)
        #                 # print('sell order:')
        #                 # print(j)
    # print(ordersDf)

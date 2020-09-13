import random
from datetime import datetime

import pandas as pd
import time

from backend.securityGenerator import equityNames, UpdateBatchSize, GetRandomPrice
from backend.randomOrderGenerator import index, indexLocked, RandomGenerator, PrintOrderDetails, RetrieveSorted

# ordersDf = RandomGenerator(100, 200)

def OrderMatching():
    ordersDf = RandomGenerator(100, 200)
    count = 0
    # print('look at this')
    # print(ordersDf[ordersDf.LOM == 'l'])
    # print('*****')'
    for srno, i in ordersDf.iterrows():
        dfIndex = pd.Index(ordersDf)
        if i.iloc[8] == 0:
            if (i.iloc[4] == 's' and i.iloc[5] == 'l'):
                # loop = True
                for sr, j in ordersDf[(ordersDf.BOS != 's') & (ordersDf.done == 0)].iterrows():
                    print(len(ordersDf.index))
                    # if loop == False:
                    #     break
                    if j.iloc[6] >= i.iloc[6] and i.iloc[1] == j.iloc[1]:
                        if i.iloc[2] == j.iloc[2]:
                            # ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
                            # ordersDf = ordersDf[ordersDf.id != str(i.iloc[0])]
                            # time.sleep(0.25)
                            # ordersDf = ordersDf[ordersDf.id != str(j.iloc[0])]
                            # ordersDf = ordersDf[~ordersDf.index.isin(dfIndex.get_loc(ordersDf.id == str(i.iloc[0])))]
                            ordersDf = ordersDf[~ordersDf.index.isin([3])]
                            time.sleep(3)
                            # ordersDf = ordersDf[~(ordersDf.id == str(j.iloc[0]))]
                            # ordersDf = ordersDf[~ordersDf.index.isin(dfIndex.get_loc(ordersDf.id == str(j.iloc[0])))]
                            ordersDf = ordersDf[~ordersDf.index.isin([4])]

                            time.sleep(3)
                            print('s l order executed')
                            count=count+1
                            # loop = False
                            # break
            # elif (i.iloc[4] == 's' and i.iloc[5] == 'm'):
            #     loop = True
            #     tempDf = RetrieveSorted(0)
            #     for sr, j in tempDf.iterrows():
            #         if loop == False:
            #             break
            #         if (str(i.iloc[2]) == str(j.iloc[2])) and (str(i.iloc[1]) == str(j.iloc[1])):
            #             ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
            #             print('s m executed')
            #             loop = False
            #             break
            # elif (i.iloc[4] == 'b' and i.iloc[5] == 'l'):
            #     loop = True
            #     for sr, j in ordersDf[ordersDf.BOS != 'b'].iterrows():
            #         if loop == False:
            #             break
            #         if j.iloc[6] <= i.iloc[6] and i.iloc[1] == j.iloc[1]:
            #             if i.iloc[2] == j.iloc[2]:
            #                 ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
            #                 print('b l order executed')
            #                 loop = False
            #                 break
            # elif (i.iloc[4] == 'b' and i.iloc[5] == 'm'):
            #     tempDf = RetrieveSorted(1)
            #     loop = True
            #     for sr, j in tempDf.iterrows():
            #         if loop == False:
            #             break
            #         if (str(i.iloc[2]) == str(j.iloc[2])) and (str(i.iloc[1]) == str(j.iloc[1])):
            #             ordersDf = ordersDf[(ordersDf.id != str(i.iloc[0])) & (ordersDf.id != str(j.iloc[0]))]
            #             print('b m executed')
            #             loop = False
            #             break
    print('orders executed '+str(count))

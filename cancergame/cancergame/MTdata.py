from cancergame import init_cancerGDV
import pandas as pd
import random as rd
import os
import gc

save_location = 'D:\\Github\\cancergame\\data\\'
list_xd = []
list_xg = []
list_xv = [] 

list_ba = []
list_bv = []
list_c = []
list_n_neigh = []
time_end = []


for t in range(10):
    for i in range(10000):
        xv = 0
        xd = 0
        xg = 0

        while xv <= 0:
            xd = rd.uniform(0, 1)
            xg = rd.uniform(0, 1)
            xv = 1-xd-xg

        ba = rd.uniform(0, 100)
        bv = rd.uniform(0, 100)
        c = rd.uniform(0, 100)
        n_neigh = int(rd.uniform(0, 100))

        time_end.append(init_cancerGDV(xd, xg, xv, ba, bv, c, n_neigh, visual=False))
        list_xd.append(xd)
        list_xg.append(xg)
        list_xv.append(xv)

        list_ba.append(ba)
        list_bv.append(bv)
        list_c.append(c)
        list_n_neigh.append(n_neigh)

        if i%100 == 0:
            print("Obtained " + str(i) + ' games.')
            df = pd.DataFrame({'xg': list_xg, 'xd': list_xd, 'xv': list_xv, 'ba': list_ba, 'bv': list_bv,  'c': list_c, 'n_neigh': list_n_neigh, 'time': time_end})
            df.to_csv(save_location+'game_time_' + str(t) + '.csv', index=False)
    
    gc.collect()
    os.system('cls||clear')
    print("Finished file: " + 'game_time_' + str(t) + '.csv')



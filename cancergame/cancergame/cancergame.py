import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

def init_cancerGDV(
    xd = 0.04, 
    xg = 0.9, 
    xv = 0.06,
    ba = 2.5,
    bv = 2,
    c = 1,
    n_neigh = 4,
    dt = 0.01,
    iter = 3000,
    rb = 10**(-1.5),
    fb = 10**(-1.5),
    sigma = 0.01, 
    d = None, timeframe = None, visual = True 
):
    """Function to plot static evolution of cancer game.

    Arguments
    ---------
        xd (float): subpopulation proportion of DEF tumor; 
            default 0.04

        xg (float): subpopulation proportion of GLY tumor; 
            default 0.9

        xv (float): subpopulation proportion of VOP tumor; 
            default 0.06

        ba (float): the benefit per unit of acidification; 
            default 2.5

        bv (float): the benefit from thge oxygen per unit of vascularization; 
            default 2

        c (float): the cost of production VEGF; default 1

        n_neigh (float): the number of GLY cells in the interaction group;
            default 4

        dt (float): time differentiation; 
            default 0.0001

        iter (int): tumors' evolutionary time dependency;
            default 500000
        
        rb (float): recovery barrier;
            default 10**(-1.5)
        
        fb (float): failure barrier;
            default 10**(-1.5)
        
        d (list): constraint medicine; 
            default None
        
        timeframe (list): update timeframe for injecting medicine;
            default None

        sigma (float): penalty for medicine computation;
            default 0.01
    Returns
    -------
        2 matplotlib figure objects containing the designated simplex (3D and 2D).
    """

    # Evolution of subpopulation propotions
    xdpoints = [xd]
    xgpoints = [xg]
    xvpoints = [xv]
    ppoints = [xg]
    qpoints = [xv/(xv + xd)]
    rate_p = []
    rate_q = []
  

    # game_proceed = 1
    win = []
    
    succeed = rb
    fail = 1-fb

    q = xv/(xv + xd)
    p = xg
    # start_time = time.time()
    t = 0
    # for t in range(iter):
    while True:
      prev_q = q
      prev_p = p

      dq = 0
      dp = 0
      sum_p = 0

      for k in range(0, n_neigh):
        sum_p += p**k
      dq = q * (1 - q) * (bv/(n_neigh+1) * sum_p - c) * dt
      q += dq
      
      # Replicator dynamic in 2-D transformation
      if timeframe != None:
        for i in range(len(timeframe)):
          if t >= timeframe[i][0] and t <= timeframe[i][1]:
            dp = p * (1 - p) * (ba/(n_neigh+1) - (bv - c) * prev_q - d) * dt
            temp_opt = (ba/(n_neigh+1) - d)/(bv - c) - prev_q
            print("Time: " + str(t) + ". Optimisation: " + str(temp_opt))
            break
          else:
            dp =  p * (1 - p) * (ba/(n_neigh+1) - (bv - c) * prev_q) * dt
      else:
        dp =  p * (1 - p) * (ba/(n_neigh+1) - (bv - c) * prev_q) * dt
      p += dp

      # Convert from 2-D to 3-D
      xd = (1 - q) * (1 - p)
      xg = p
      xv = (1 - p) * q

      ppoints.append(p)
      qpoints.append(q)

      rate_p.append(dp)
      rate_q.append(dq)

      xdpoints.append(xd)
      xgpoints.append(xg)
      xvpoints.append(xv)

      
      
      # Terminal condition
      if p <= succeed:
        win = 1
        # print("Treatment succeed at " + str(t*dt))
        break
          
      elif p >= fail:
        win = 0
        # print("Treatment fail at " + str(t*dt))
        break
      
      t += 1

    total_cost = 0
    # Total cost for the treatment
    # total_cost = 0
    # if timeframe != None:
      # for i in range(len(timeframe)):
        # time_treatment = (timeframe[i][1]-timefrae)*dt
      # print("Total time treatment: ", time_treatment)

      # total_cost = time_treatment*(d+sigma) + sigma*timelow*dt
      # total_cost = time_treatment*(d+sigma)
      # print("Total cost: ", total_cost)

    # print("Time: ", t)

    fig_2D, fig_3D = None, None
    if visual == True: 
      # 2D visualization
      fig_2D = plt.figure(figsize=(15,7))
      plt.axhline(succeed, color="g", linestyle='dashed', label="Succeed barrier")
      plt.axhline(fail, color="r", linestyle='dashed', label="Fail barrier")
    
      length = len(xgpoints)
      plt.plot(xgpoints, label="GLY", color="purple")
      plt.plot(xdpoints, label="DEF", color="royalblue")
      plt.plot(xvpoints, label="VOP", color="orange")

      # plt.plot(rate_p, label="p")
      # plt.plot(rate_q, label="q")

      if timeframe != None:
        for i in range(len(timeframe)):
          plt.axvspan(timeframe[i][0], timeframe[i][1], facecolor="red", alpha=0.15)

      plt.xlabel("Time", fontweight="bold", fontsize='x-large')
      plt.xlim(0, t)
      plt.xticks(np.arange(0, t, 500), np.arange(0, t*dt, 500*dt))
      plt.ylim(0, 1)
      plt.ylabel("Subpopulation proportions", fontweight="bold", fontsize='x-large')
      plt.legend()

      # 3D visualization
      dynamic = []
      dynamic.append(xdpoints)
      dynamic.append(xgpoints)
      dynamic.append(xvpoints)
      dynamic = np.array(dynamic)
      dynamic = dynamic.transpose()
      fail = fail*(np.sqrt(3)/2)
      succeed = succeed*(np.sqrt(3)/2)
      # print(fail)

      transformation = np.array([[1,0],
                                [0.5, np.sqrt(3)/2],
                                [0,0]])
      dynamic_2D = np.matmul(dynamic, transformation)

      fig_3D = plt.figure(figsize=(7,7))
      plt.plot([1,0,0.5,1], [0,0,np.sqrt(3)/2,0])
      plt.plot(dynamic_2D[:, 0], dynamic_2D[:, 1], color='g', label="No therapy")

      if timeframe != None:
        for i in range(len(timeframe)):
          plt.plot(dynamic_2D[timeframe[i][0]:timeframe[i][1], 0], dynamic_2D[timeframe[i][0]:timeframe[i][1], 1], color='r', label="Therapy applied")
      plt.ylim(0, 1)
      plt.xlim(0, 1)

      plt.axhline(succeed, color="g", linestyle='dashed', label="Succeed barrier")
      plt.axhline(fail, color="r", linestyle='dashed', label="Fail barrier")
    else:
      return t

    return fig_2D, fig_3D, total_cost
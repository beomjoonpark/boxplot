#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
import csv


plt.rcParams['font.family'] = 'Times New Roman'

def get_data(pathname):
    tlist = []
    plist = []
    with open(pathname) as csvfile:
        reader = csv.reader(csvfile)
        h = 0
        xidx = 0
        for row in reader:
            if h == 0:
                h = 1
                continue

            tlist.append(float(row[2]))

            if xidx == 0:
                try:                        # to cover both PoseStamped and Odometry types
                    _ = float(row[4])
                    xidx = 4
                except:
                    xidx = 5
            
            plist.append((float(row[xidx]), float(row[xidx+1]), float(row[xidx+2])))


    return [tlist, plist]

def get_error(ref, data):
    errorlist = []

    for i in range(len(data[0])):
        t = data[0][i]
        d = data[1][i]

        diff_list = []
        for j in range(len(ref[0])):
            # print(t, ref[0][j])
            if ref[0][j] >= t-10000000 and ref[0][j] <= t+10000000:         # t_max_diff=0.01
                diff = np.linalg.norm(np.array(d)-np.array(ref[1][j]))
                diff_list.append(diff)
            elif ref[0][j] > t+10000000:
                break

        if diff_list:
            errorlist.append(min(diff_list))
        else:

            pass
    print(len(data[0]))
    print(len(errorlist))
    return np.array(errorlist), np.sqrt(np.mean(np.square(errorlist)))

# def get_error(ref, data):
#     errorlist = []

#     for i in range(len(data[0])):
#         t = data[0][i]
#         d = data[1][i]

#         for j in range(len(ref[0])):
#             if ref[0][j] >= t:
#                 diff1 = np.linalg.norm(np.array(d)-np.array(ref[1][j-1]))
#                 diff2 = np.linalg.norm(np.array(d)-np.array(ref[1][j]))
#                 errorlist.append(min(diff1, diff2))
#                 break

#     return np.array(errorlist), np.sqrt(np.mean(np.square(errorlist)))
            
            



def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color, linewidth=3.0)
    plt.setp(bp['whiskers'], color=color, linewidth=3.0)
    plt.setp(bp['caps'], color=color, linewidth=3.0)
    plt.setp(bp['medians'], color=color, linewidth=3.0)
    # plt.setp(bp['fliers'], markeredgecolor=color)



def boxplot(name, data, method_name, drone_name, color_list, yrange):

    plt.figure(figsize=(16, 8))

    n = len(method_name)
    offset = 3.2/(n-1)
    
    plotlist = []
    for i in range(len(method_name)):
        p = plt.boxplot(data[i], positions=np.array(xrange(len(data[i])))*6.0-1.6+i*offset,
                         sym='', widths=0.6, whiskerprops=dict(linestyle='--'))
        set_box_color(p, color_list[i])
        plt.plot([], c=color_list[i], label=method_name[i])
        
        plotlist.append(p)
    leg = plt.legend(loc='upper left', fontsize=20)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(3.0)

    plt.xticks(xrange(0, len(drone_name)*6, 6), drone_name, fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim(-3, (len(drone_name)-1)*6+3)
    plt.ylim(yrange[0], yrange[1])
    # plt.title(name)
    plt.xlabel("Robot ID", fontsize=20)
    plt.ylabel("Translation error [m]", fontsize=20)
    plt.show()


def test():
    method1_data = [[1,2,5], [5,7,2,2,5], [7,2,5], [5,7,2,2,5], [7,2,5]]
    method2_data = [[6,4,2], [1,2,5,3,2], [2,3,5,1], [5,7,2,2,5], [7,2,5]]
    method3_data = [[1,2,5], [5,7,2,2,5], [7,2,5], [5,7,2,2,5], [7,2,5]]
    method4_data = [[6,4,2], [1,2,5,3,2], [2,3,5,1], [5,7,2,2,5], [7,2,5]]
    
    exp_name = "exp1"

    drone= ['UAV1', 'UAV2', 'UAV3', 'UAV5', 'UGV1']

    data = [method1_data, method2_data, method3_data, method4_data]
    method= ['A', 'B', 'C', 'D']
    color= ['red', 'blue', 'yellow', 'green']


    boxplot(exp_name, data, method, drone, color, (-10, 10))



# test()
if __name__ == '__main__':

    method = ["ours", "sota1", "sota2", "vins"]
    cmp = ["gps", "s1gps", "s2gps", "gps"]
    robot1 = ["UAV1", "UAV2", "UAV3", "UAV5", "UGV1"]
    robot2 = ["UAV1", "UAV2", "UAV3", "UAV4", "UAV5"]

    exp1_w_error = []
    exp1_w_rmse = []
    for i in range(4):
        m = method[i]
        g = cmp[i]
        error_l = []
        rmse_l = []
        for r in robot1:
            data = get_data("./exp1/exp1_"+r+"_"+m+".csv")
            ref = get_data("./exp1/exp1_"+r+"_"+g+".csv")
            error, rmse = get_error(ref, data)
            error_l.append(error)
            rmse_l.append(rmse)
        exp1_w_error.append(error_l)
        exp1_w_rmse.append(rmse_l)
        print(m, rmse_l)
    print("")


    # exp1_wo_error = []
    # exp1_wo_rmse = []
    # for i in range(3):
    #     m = method[i]
    #     g = cmp[i]
    #     error_l = []
    #     rmse_l = []
    #     for r in robot1:
    #         data = get_data("./exp1_wo/exp1_"+r+"_"+m+".csv")
    #         ref = get_data("./exp1_wo/exp1_"+r+"_"+g+".csv")
    #         error, rmse = get_error(ref, data)
    #         error_l.append(error)
    #         rmse_l.append(rmse)
    #     exp1_wo_error.append(error_l)
    #     exp1_wo_rmse.append(rmse_l)
    #     print(m, rmse_l)
    # print("")


    exp2_w_error = []
    exp2_w_rmse = []
    for i in range(4):
        m = method[i]
        g = cmp[i]
        error_l = []
        rmse_l = []
        for r in robot2:
            data = get_data("./exp2/exp2_"+r+"_"+m+".csv")
            ref = get_data("./exp2/exp2_"+r+"_"+g+".csv")
            error, rmse = get_error(ref, data)
            error_l.append(error)
            rmse_l.append(rmse)
        exp2_w_error.append(error_l)
        exp2_w_rmse.append(rmse_l)
        print(m, rmse_l)
    print("")


    exp2_wo_error = []
    exp2_wo_rmse = []
    for i in range(4):
        m = method[i]
        g = cmp[i]
        error_l = []
        rmse_l = []
        for r in robot2:
            data = get_data("./exp2_wo/exp2_"+r+"_"+m+".csv")
            ref = get_data("./exp2_wo/exp2_"+r+"_"+g+".csv")
            error, rmse = get_error(ref, data)
            error_l.append(error)
            rmse_l.append(rmse)
        exp2_wo_error.append(error_l)
        exp2_wo_rmse.append(rmse_l)
        print(m, rmse_l)
    print("")

    






    
    exp_name1 = "Experiment 1, with init"
    drone1= ['1', '2', '3', '4', '5']

    method1= ['Proposed', 'Flexible [13]', 'UWB-VIO Fusion [14]', "VINS-Fusion [1]"]
    color1= ['red', 'blue', 'green', 'goldenrod']


    boxplot(exp_name1, exp1_w_error, method1, drone1, color1, (0, 30))




    # exp_name1_wo = "Experiment 1, without init"
    # drone1_wo= ['1', '2', '3', '4', '5']

    # method1_wo= ['Proposed', 'Flexible [13]', 'UWB-VIO Fusion [14]', "VINS-Fusion [1]"]
    # color1_wo= ['red', 'blue', 'green', goldenrod]


    # boxplot(exp_name1_wo, exp1_wo_error, method1_wo, drone1_wo, color1_wo, (0, 30))




    exp_name2 = "Experiment 2"
    drone2= ['1', '2', '3', '4', '5']

    method2= ['Proposed', 'Flexible [13]', 'UWB-VIO Fusion [14]', "VINS-Fusion [1]"]
    color2= ['red', 'blue', 'green', 'goldenrod']


    boxplot(exp_name2, exp2_w_error, method2, drone2, color2, (0, 15))




    exp_name2_wo = "Experiment 2, without init"
    drone2_wo= ['1', '2', '3', '4', '5']

    method2_wo= ['Proposed', 'Flexible [13]', 'UWB-VIO Fusion [14]', "VINS-Fusion [1]"]
    color2_wo= ['red', 'blue', 'green', 'goldenrod']


    boxplot(exp_name2_wo, exp2_wo_error, method2_wo, drone2_wo, color2_wo, (0, 25))

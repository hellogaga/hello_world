# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:46:00 2017

@author: ZY
"""

import sched, time


s = sched.scheduler(time.time, time.sleep)


def function1 (cc,dd):
    global ee
    ee=[]
    ee.append(cc+dd)
    ee.append(cc+dd+dd)
#    return ee, ff


def print_some_times():
    Epoch_Time = time.time()
    Min5_Time=Epoch_Time/300
    Start_Epoch_Time= (int (Min5_Time)+1)*300
    St_Local_Time=time.localtime(Start_Epoch_Time) 
    print time.time()
    s.enterabs(Start_Epoch_Time, 1, function1, (4,5))
#    s.enter(10, 1, print_time, ())
    s.run()
#    print time.time()


print_some_times()
print ee

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:00:47 2017

@author: ZY
"""

import sched, time
import Adafruit_DHT

s = sched.scheduler(time.time, time.sleep)
#def print_time(): print "From print_time", time.time()

###############################################################################
# This is the funtion to record the temperature sensor data. It should be executed
# every five minutes. It takes five minutes to finish (It measures average values)
# The measured results will be directly recorded. 
def Read_Log_Data (Pin_22Sensor, Pin_11Sensor, Exe_Epoch_Time):   
    import numpy as np
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    
    Humidity_record_22=[]
    Tem_record_22=[]
    Humidity_record_11=[]
    Tem_record_11=[]      
    for i in range(3):
        humidity22, temperature22 = Adafruit_DHT.read_retry(22, Pin_22Sensor)
        time.sleep(0.5)
        humidity11, temperature11 = Adafruit_DHT.read_retry(11, Pin_11Sensor)
    
        if humidity22 is not None and temperature22 is not None:
            Humidity_record_22.append(humidity22)
            Tem_record_22.append(temperature22)
            
        if humidity11 is not None and temperature11 is not None:
            Humidity_record_11.append(humidity11)
            Tem_record_11.append(temperature11)        
        
        time.sleep(50)
        
    global Aver_Hum_22, Aver_Tem_22, Aver_Hum_11,  Aver_Tem_11
    Aver_Hum_22=np.mean(Humidity_record_22)
    Aver_Tem_22=np.mean(Tem_record_22)
    Aver_Hum_11=np.mean(Humidity_record_11)
    Aver_Tem_11=np.mean(Tem_record_11) 
    Exe_Local_Time=time.localtime(Exe_Epoch_Time) # The local time of starting the record
    Txt_file_Name=time.strftime("%Y-%m-%d", Exe_Local_Time)+'.txt'
    
    f = open(Txt_file_Name, 'a')
    f.write('\n')
    f.write ('%.3f' % Exe_Epoch_Time)
    f.write (',')    
    Exe_Local_Time_String=time.strftime("%A, %Y-%m-%d, %H:%M:%S,", Exe_Local_Time)
    f.write(Exe_Local_Time_String)
    
    Strings_Text= '%.3f' % Aver_Hum_22+ ',' + '%.3f' % Aver_Tem_22+ ','+ '%.3f' % Aver_Hum_11+ ','+'%.3f' % Aver_Tem_11+ ','
    f.write(Strings_Text)
    Finish_Epoch_Time=time.time()
    Finish_Local_Time=time.localtime(Finish_Epoch_Time)
    f.write ('%.3f' % Finish_Epoch_Time)
    f.write (',')  
    Finish_Local_Time_String=time.strftime("%A, %Y-%m-%d, %H:%M:%S,", Finish_Local_Time)
    f.write(Finish_Local_Time_String)
    f.close()
    
    del Aver_Hum_22, Aver_Tem_22, Aver_Hum_11, Aver_Tem_11
    
#    GPIO.cleanup()
    
#    return Aver_Hum_22, Aver_Tem_22, Aver_Hum_11, Aver_Tem_11
    


Epoch_Time = time.time()
Min5_Time=Epoch_Time/300
Start_Epoch_Time= (int (Min5_Time)+1)*300
 # The local time of starting the record

while True:
    print "The next recording starts: ", time.localtime(Start_Epoch_Time)
    s.enterabs(Start_Epoch_Time, 1, Read_Log_Data, (4,5, Start_Epoch_Time))
    s.run()
    print "The recording finishing time is:", time.localtime()
    Start_Epoch_Time=Start_Epoch_Time+300
    
   
                  
                 
                  
                  
                  
#print time1
#for interval in range (24*5)
#    s.enter(60*5, 1, Read_Log_Data, (4,5, time1+5))    
#    time1=time1+60;
#s.run()
#
#
#print time.time()

#def print_some_times():
#    time1= time.time()
#    print time1
#    s.enter(5, 1, ReadData, (4,5, time1+5))    
#    s.run()
#    
#    print time.time()
#    
#print_some_times()

#from time import strftime, time, gmtime
#strftime("%A, %j, %Y-%m-%d, %H:%M:%S", gmtime(time()+3600))
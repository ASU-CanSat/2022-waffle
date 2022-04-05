"""
@file   csv_generation.py
@author Emil Roy

This file contains the CSV Generation file.
"""
import csv
from csv import writer

#create the 2 csv files required
def build():
    #write to container csv file
    with open('reports/Flight_1052_C.csv', 'w', newline='') as file:
        writerC = csv.writer(file)
        #create the csv headers
        writerC.writerow(['TEAM_ID','MISSION_TIME','PACKET_COUNT','PACKET_TYPE','MODE',
                        'TP_RELEASED','ALTITUDE','TEMP',
                        'VOLTAGE','GPS_TIME','GPS_LATITUDE','GPS_LONGITUDE',
                        'GPS_ALTITUDE','GPS_SATS','SOFTWARE_STATE','CMD_ECHO'])
        file.close()

    #write to payload csv file
    with open('reports/Flight_1052_T.csv', 'w', newline='') as file:
        writerTP = csv.writer(file)
        #create the csv headers
        writerTP.writerow(['TEAM_ID','MISSION_TIME','PACKET_COUNT','PACKET_TYPE',
                            'TP_ALTITUDE','TP_TEMP','TP_VOLTAGE','GYRO_R','GYRO_P'
                            'GYRO_Y','ACCEL_P','ACCEL_P','ACCEL_Y','MAG_R','MAG_P','MAG_Y', 
                            'POINTING_ERROR','TP_SOFTWARE_STATE'])
        file.close()

#to append data to the csv files
def append_csv_file(line):
    data = line.split(",")
    type = data[3] #to check if it came from container or payload
    #appends data to the proper csv file
    if type == 'C':
        with open('reports/Flight_1052_C.csv', 'a', newline='') as file:
            writer_object = writer(file)
            writer_object.writerow(data)
            file.close()
    if type == 'T':
        with open('reports/Flight_1052_T.csv', 'a', newline='') as file:
            writer_object = writer(file)
            writer_object.writerow(data)
            file.close()
    else: #should there be some errors?
        pass

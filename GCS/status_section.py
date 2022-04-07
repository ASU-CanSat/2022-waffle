"""
@file   status_section.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants

time = "time not set!"
missionTimeLabel = QLabel("Mission Time (UTC): " + time)

simulationLabel = QLabel("Simulation Mode Status: False")
simulationLabel.setStyleSheet("color: red")

mqttTransmitLabel = QLabel("MQTT Transmission Status: False")
mqttTransmitLabel.setStyleSheet("color: red")

payload1Label = QLabel("Tethered Payload Is NOT Deployed")
payload1Label.setStyleSheet("color: red")

# returns a layout that can be included in application window
def build():

    # can add future labels here such as altitude, temperature, etc if wanted

    #adding all the widgets to the layout
    layout = QVBoxLayout()
    layout.addWidget(missionTimeLabel)
    layout.addWidget(simulationLabel)
    layout.addWidget(mqttTransmitLabel)

    return layout

#function to update simulation status
def simulationStatus(enable, activate):
    if (enable == True and activate == True):
        simulationLabel.setText("Simulation Mode Status: True")
        simulationLabel.setStyleSheet("color: green")
    else:
        simulationLabel.setText("Simulation Mode Status: False")
        simulationLabel.setStyleSheet("color: red")

#function to update MQTT transmission status
def mqttStatus(status):
    if (status == False):
        mqttTransmitLabel.setText("MQTT Transmission Status: False")
        mqttTransmitLabel.setStyleSheet("color: red")
    else:
        mqttTransmitLabel.setText("MQTT Transmission Status: True")
        mqttTransmitLabel.setStyleSheet("color: green")

def updateMissionTime(packet):
    global time
    packet_args = packet.split(",")
    time = packet_args[1]

def update():
    missionTimeLabel.setText("Mission Time (UTC): " + time)
    
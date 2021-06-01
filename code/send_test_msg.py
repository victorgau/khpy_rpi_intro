# -*- coding: utf-8 -*-

# 如果沒有安裝 paho-mqtt，記得 pip install paho-mqtt
import paho.mqtt.client as mqtt
import time
import random

n = 1

# broker = "iot.eclipse.org" 
broker = "broker.hivemq.com"
client = mqtt.Client("client_"+str(random.random()))
client.connect(broker)

while True:
    for i in range(n):
        T = str(random.randint(25,30))
        H = str(random.randint(50,70))
        print(f"{i} sending ==> 溫度：{T}, 濕度：{H}")
        client.publish(f"wetland/sensor/{i}/溫度", T)
        client.publish(f"wetland/sensor/{i}/濕度", H)
    time.sleep(5)

# 樹莓派(Raspberry Pi)使用簡介

## 關於唯客學院：

* [唯客學院網址](http://www.vcdemy.com)
* [唯客學院粉絲團](https://www.facebook.com/KHPYAcademy/)
* [唯客學院線上課程](https://khpy.teachable.com)

## 教學影片

* [樹莓派簡介](https://www.youtube.com/playlist?list=PLj4JWjo5dOC6Ec1GVeNoOMWilvKt99LlU)

## 課程內容：

### 1. 文件導覽：

* [Raspberry Pi 官網](https://www.raspberrypi.org/)
* [Raspberry Projects](https://projects.raspberrypi.org/)
* [Raspberry Pi Imager](https://www.raspberrypi.org/software/)
* [Raspberry Pi Remote Access](https://www.raspberrypi.org/documentation/remote-access/)
* [Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)

### 2. 實作引導：

* [如何燒錄OS到MicroSD卡上？](https://www.raspberrypi.org/software/)
* 如果有螢幕、鍵盤、滑鼠，可以接上RPi然後插上電源使用看看。
* 沒有鍵盤、滑鼠和螢幕要怎麼連線 (Headless Connection)？
  * 預設域名：raspberrypi.local
  * 預設帳號：pi
  * 預設密碼：raspberry
* [找不到預設的域名(raspberrypi.local)怎麼辦？](https://www.raspberrypi.org/documentation/remote-access/ip-address.md)
* SSH連線(使用內建SSH或puTTY)
* [VNC連線(圖形化介面)](https://www.realvnc.com/en/connect/download/viewer/)
* [安裝Visual Studio Code](https://code.visualstudio.com/)
* [SCP的使用(拷貝資料到RPi上面)](https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md)
* [遠端開發(Remote Development)](https://code.visualstudio.com/docs/remote/ssh)
* 從RPi發送Line Notify 訊息
* [MQTT簡介](https://www.hivemq.com/)
* 設定發送(Publish)訊息至MQTT Broker
* [安裝VSC的Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
* 設定接收(Subscribe)自MQTT Broker的訊息
* [GPIO簡介](https://www.raspberrypi.org/documentation/usage/gpio)
* 使用DHT11, 22量測溫溼度(安裝adafruit_circuitpython_dht套件)
* 用 RPi Camera 擷取影像
* 用 RPi Camera 做影音串流

### 3. 自我挑戰：

* 使用DHT11或DHT22量測溫溼度，透過MQTT送到主控台顯示。
* 使用 raspivid 做影音串流，並在筆電上用 opencv 讀取串流影片下來做分析。

### 相關連結：

* [PuTTY](https://www.putty.org/)
* [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)
* [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
* [Chrome上面之後不會有VNC Viewer App囉！](https://help.realvnc.com/hc/en-us/articles/360017492037-Product-End-of-Life-EoL-notice-#vnc-viewer-plus-0-0)
* [HiveMQ](https://www.hivemq.com/)
* [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)
* [fritzing](https://fritzing.org/)
* [Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)
* [Adafruit CircuitPython DHT Library](https://circuitpython.readthedocs.io/projects/dht/en/latest/index.html)
* [10 Free Public MQTT Brokers](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/)
* [Beginner’s Guide To Using Paho-MQTT, A Python MQTT Client](https://mntolia.com/mqtt-python-with-paho-mqtt-client/)
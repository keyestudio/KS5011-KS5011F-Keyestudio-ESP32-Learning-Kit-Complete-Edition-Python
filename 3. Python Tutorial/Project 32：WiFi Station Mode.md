**Project 32：WiFi Station Mode**

1.  **Introduction**

ESP32 has three different WiFi operating modes : Station mode，AP mode
and AP+Station mode. All WiFi programming projects must be configured
with WiFi operating mode before using, otherwise WiFi cannot be used. In
this project, we are going to learn the WiFi Station mode of the ESP32.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/729232b0c2d2c01984808289b222890c.png" style="width:1.8125in;height:0.86458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/53f17b0de2d98d4714e8fe9043a346ca.jpeg" style="width:2.43681in;height:1.13472in" /></td>
</tr>
<tr class="even">
<td>USB Cable*1</td>
<td>ESP32*1</td>
</tr>
</tbody>
</table>

**3. Wiring Diagram**

Plug the ESP32 to the USB port of your PC

![](/media/53f17b0de2d98d4714e8fe9043a346ca.jpeg)

**4. Component Knowledge**

**Station mode：**

When setting Station mode, the ESP32 is taken as a WiFi client. It can
connect to the router network and communicate with other devices on the
router via a WiFi connection. As shown in the figure below, the PC and
the router have been connected. If the ESP32 wants to communicate with
the PC, the PC and the router need to be connected.

![](/media/f74baff97695aa2ee33a8c19370d2547.png)

5.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
32：WiFi Station Mode”，and double left-click
“Project\_32\_WiFi\_Station\_Mode.py”.

![](/media/e058260f4a2aa85d854443405839da2a.png)

<table>
<tbody>
<tr class="odd">
<td><p>import time</p>
<p>import network # Import network module.</p>
<p>ssidRouter = 'ChinaNet-2.4G-0DF0' # Enter the router name</p>
<p>passwordRouter = 'ChinaNet@233' # Enter the router password</p>
<p>def STA_Setup(ssidRouter,passwordRouter):</p>
<p>print("Setup start")</p>
<p>sta_if = network.WLAN(network.STA_IF) # Set ESP32 in Station mode.</p>
<p>if not sta_if.isconnected():</p>
<p>print('connecting to',ssidRouter)</p>
<p># Activate ESP32’s Station mode, initiate a connection request to the router</p>
<p># and enter the password to connect.</p>
<p>sta_if.active(True)</p>
<p>sta_if.connect(ssidRouter,passwordRouter)</p>
<p>#Wait for ESP32 to connect to router until they connect to each other successfully.</p>
<p>while not sta_if.isconnected():</p>
<p>pass</p>
<p># Print the IP address assigned to ESP32-WROVER in “Shell”.</p>
<p>print('Connected, IP address:', sta_if.ifconfig())</p>
<p>print("Setup End")</p>
<p>try:</p>
<p>STA_Setup(ssidRouter,passwordRouter)</p>
<p>except:</p>
<p>sta_if.disconnect()</p></td>
</tr>
</tbody>
</table>

**6. Test Result**

The names and passwords of routers in various places are different,
thereby before running the code, users need to enter the correct
router’s name and password in the box, as shown in the illustration
above.

After making sure the router name and password are entered correctly,
click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and wait for ESP32 to connect to your router and print the IP
address assigned by the router to ESP32 in the "Shell" window of Thonny
IDE.

![](/media/7a27c9cb736ba4b26ef206c0e960f772.jpeg)

![](/media/e283d185859ce0a4372c53449bfd03b8.png)

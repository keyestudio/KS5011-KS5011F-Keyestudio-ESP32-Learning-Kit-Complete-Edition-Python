**Project 34：WiFi Station+AP Mode**

1.  **Introduction**

In this project, we are going to learn the AP+Station mode of the ESP32.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/729232b0c2d2c01984808289b222890c.png" style="width:1.8125in;height:0.86458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/53f17b0de2d98d4714e8fe9043a346ca.jpeg" style="width:2.43681in;height:1.13472in" /></td>
</tr>
<tr class="even">
<td> USB Cable*1</td>
<td>ESP32*1</td>
</tr>
</tbody>
</table>

**3. Wiring Diagram**

Plug the ESP32 mainboard to the USB port of your PC

![](/media/53f17b0de2d98d4714e8fe9043a346ca.jpeg)

**4. Component Knowledge**

**AP+Station mode:**

In addition to the AP mode and the Station mode, **AP+Station mode** can
be used at the same time. Turn on the Station mode of the ESP32, connect
it to the router network, and it can communicate with the Internet
through the router. Then turn on the AP mode to create a hotspot
network. Other WiFi devices can be connected to the router network or
the hotspot network to communicate with the ESP32.

**5. Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the code in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
34：WiFi Station+AP Mode”，and double left-click
“Project\_34\_WiFi\_Station+AP\_Mode.py”.

![](/media/1ec034a81c5f59b5c6568974db3eda91.png)

<table>
<tbody>
<tr class="odd">
<td><p>import network #Import network module.</p>
<p>ssidRouter = 'ChinaNet-2.4G-0DF0' #Enter the router name</p>
<p>passwordRouter = 'ChinaNet@233' #Enter the router password</p>
<p>ssidAP = 'ESP32_WiFi'#Enter the AP name</p>
<p>passwordAP = '12345678' #Enter the AP password</p>
<p>local_IP = '192.168.4.147'</p>
<p>gateway = '192.168.1.1'</p>
<p>subnet = '255.255.255.0'</p>
<p>dns = '8.8.8.8'</p>
<p>sta_if = network.WLAN(network.STA_IF)</p>
<p>ap_if = network.WLAN(network.AP_IF)</p>
<p>def STA_Setup(ssidRouter,passwordRouter):</p>
<p>print("Setting soft-STA ... ")</p>
<p>if not sta_if.isconnected():</p>
<p>print('connecting to',ssidRouter)</p>
<p>sta_if.active(True)</p>
<p>sta_if.connect(ssidRouter,passwordRouter)</p>
<p>while not sta_if.isconnected():</p>
<p>pass</p>
<p>print('Connected, IP address:', sta_if.ifconfig())</p>
<p>print("Setup End")</p>
<p>def AP_Setup(ssidAP,passwordAP):</p>
<p>ap_if.ifconfig([local_IP,gateway,subnet,dns])</p>
<p>print("Setting soft-AP ... ")</p>
<p>ap_if.config(essid=ssidAP,authmode=network.AUTH_WPA_WPA2_PSK, password=passwordAP)</p>
<p>ap_if.active(True)</p>
<p>print('Success, IP address:', ap_if.ifconfig())</p>
<p>print("Setup End\n")</p>
<p>try:</p>
<p>AP_Setup(ssidAP,passwordAP)</p>
<p>STA_Setup(ssidRouter,passwordRouter)</p>
<p>except:</p>
<p>sta_if.disconnect()</p>
<p>ap_if.idsconnect()</p></td>
</tr>
</tbody>
</table>

**6. Test Result**

Before running the code, you need to modify ssidRouter, passwordRouter,
ssidAP and passwordAP.

After making sure that the code is modified correctly,
click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script” the code starts to be
executed and the“Shell”window of Thonny IDE will display as follows:

![](/media/03c30dc4b3acc21f4f81e9f3f8718b39.jpeg)

![](/media/72c864c57de3f40d2a55ee3c10449898.png)

Turn on the WiFi scanning function of your phone, and you can see the
ssidAP on ESP32.

![](/media/3e0ad895bea7f5100cc02a415adcace7.png)

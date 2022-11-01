**Project 33：WiFi AP Mode**

1.  **Introduction**

In this project, we are going to learn the WiFi AP mode of the ESP32.

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

Plug the ESP32 mainboard to the USB port of your PC

![](/media/53f17b0de2d98d4714e8fe9043a346ca.jpeg)

**4. Component Knowledge**

**AP Mode:**

When setting AP mode, a hotspot network will be created, waiting for
other WiFi devices to connect. As shown below:

Take the ESP32 as the hotspot, if a phone or PC needs to communicate
with the ESP32, it must be connected to the ESP32's hotspot.
Communication is only possible after a connection is established via the
ESP32.

![](/media/35d90f1ce10814ea1897ba63f8bd7ad9.png)

5.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
33：WiFi AP Mode”, and double left-click
“Project\_33\_WiFi\_AP\_Mode.py”.

![](/media/a0a840736509cc23d652317a424bea50.png)

<table>
<tbody>
<tr class="odd">
<td><p>import network #Import network module.</p>
<p>#Enter correct router name and password.</p>
<p>ssidAP = 'ESP32_WiFi' #Enter the router name</p>
<p>passwordAP = '12345678' #Enter the router password</p>
<p>local_IP = '192.168.1.147'</p>
<p>gateway = '192.168.1.1'</p>
<p>subnet = '255.255.255.0'</p>
<p>dns = '8.8.8.8'</p>
<p>#Set ESP32 in AP mode.</p>
<p>ap_if = network.WLAN(network.AP_IF)</p>
<p>def AP_Setup(ssidAP,passwordAP):</p>
<p>ap_if.ifconfig([local_IP,gateway,subnet,dns])</p>
<p>print("Setting soft-AP ... ")</p>
<p>ap_if.config(essid=ssidAP,authmode=network.AUTH_WPA_WPA2_PSK, password=passwordAP)</p>
<p>ap_if.active(True)</p>
<p>print('Success, IP address:', ap_if.ifconfig())</p>
<p>print("Setup End\n")</p>
<p>try:</p>
<p>AP_Setup(ssidAP,passwordAP)</p>
<p>except:</p>
<p>print("Failed, please disconnect the power and restart the operation.")</p>
<p>ap_if.disconnect()</p></td>
</tr>
</tbody>
</table>

**6. Test Result**

Before running the code, you can make any changes to the AP name and
password for ESP32 in the box as shown in the illustration above. Of
course, you can leave it alone by default.

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and open the AP function of ESP32 and print the access point
information in the "Shell" window of Thonny IDE.

![](/media/842a756a3d104aa739698b4747012053.jpeg)

![](/media/5be2d032c8adcb2976c1640268919790.png)

Turn on the WiFi scanning function of your phone, and you can see the
ssid\_AP on ESP32, which is called "ESP32\_Wifi" in this code. You can
enter the password "12345678" to connect it or change its AP name and
password by modifying Code.

![](/media/3e0ad895bea7f5100cc02a415adcace7.png)

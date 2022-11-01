**Project 25：****Human Induction Lamp**

**1.****Introduction**

Human body induction lamp is used commonly in the dark corridor area.
With the development of science and technology, the use of the human
body induction lamp is very common in our real life, such as the
corridor of the community, the bedroom of the room, the garage of the
dungeon, the bathroom and so on.

In this project, we will learn how to use a PIR motion sensor, a LED,
and a photoresistor to make a human induction lamp.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c62c393e0f1d6a2c7dc297e4ccf9b595.jpeg" style="width:1.22153in;height:0.59653in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.75972in;height:1.8625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7eb361d680dfa351f07f8527aeb37abd.png" style="width:0.275in;height:1.17361in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/8cf9b1b3a5fec374cde3c5f0537567cb.png" style="width:0.21042in;height:0.94583in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/82b6a0e286b6ca25c06c6353397bad79.png" style="width:0.19097in;height:1.26597in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/99272d75b3f952a0c2dd770e2f6f5a7c.png" style="width:1.25347in;height:0.94097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/51ab4ab6eefe8ba8f66234989d5282de.png" style="width:0.21736in;height:0.95833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/849dad1bcb5c3177310976501fbc96c9.png" style="width:1.14583in;height:0.96806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>Photoresistor*1</td>
<td>PIR Motion Sensor*1</td>
<td>220ΩResistor*1</td>
<td>M-F Dupont Wires</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Wiring Diagram**
    
    ![](/media/69f49d65054a9246acf4adc534217027.png)

4.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
25：Human Induction Lamp”，and then double left-click
“Project\_25\_Human\_ Induction\_Lamp.py”.

![](/media/6f5857ddbf0ed961db221b132bce29c4.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC</p>
<p>import time</p>
<p># Human infrared sensor pin</p>
<p>human = Pin(15, Pin.IN)</p>
<p># Initialize the photosensitive sensor pin to GP36 (ADC function)</p>
<p>adc=ADC(Pin(36))</p>
<p>adc.atten(ADC.ATTN_11DB)</p>
<p>adc.width(ADC.WIDTH_10BIT)</p>
<p>#create the LED object from Pin 4, Set Pin 4 to output</p>
<p>led = Pin(4, Pin.OUT)</p>
<p>def detect_someone():</p>
<p>if human.value() == 1:</p>
<p>return True</p>
<p>return False</p>
<p>abc = 0</p>
<p>while True:</p>
<p>adcVal=adc.read()</p>
<p>if adcVal &gt;= 500:</p>
<p>if detect_someone() == True:</p>
<p>abc += 1</p>
<p>led.value(1)</p>
<p>print("value=", abc)</p>
<p>time.sleep(1)</p>
<p>else:</p>
<p>if abc != 0:</p>
<p>abc = 0</p>
<p>led.value(0)</p>
<p>else:</p>
<p>led.value(0)</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/bbdaf50534db57036e34af09f5dc7b09.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that When your hand covers the photosensitive
part of the photoresistor to simulate darkness, then shake your other
hand in front of the PIR motion sensor, the LED will light up, and after
a few seconds, the LED will automatically turn off.  

At the same time, the "Shell" window of Thonny IDE will print the delay
time when the LED lights up. If the photosensitive part of the
photoresistor is not covered, then shake your hand in front of the PIR
motion sensor and the LED will be off. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/d6fe49c1a8e901b8e7dcc4deaee954d7.png)

![](/media/af94ad9d2f008956592ee64e207aa8b5.png)

**Project 05：Traffic Lights**

1.  **Introduction**

Traffic lights are closely related to people's daily lives, which
generally show red, yellow, and green. In this project, we will use
ESP32 and some LEDs (red, green and yellow) to simulate the traffic
lights.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c1a470aaea31f177097eacbcb17ee4c4.jpeg" style="width:1.21736in;height:0.59444in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/b57b4057770f0bcc43f037c0ab8e1c41.png" style="width:0.84375in;height:2.23125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/afa6edd3ff90b027a6f43995a6fb15a2.png" style="width:0.28333in;height:1.20972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/0c1b0f91b4e56bcbc235d06b48809ac9.png" style="width:0.27986in;height:1.22222in" /></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Red LED*1</td>
<td>Yellow LED*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/6c688493b558ed5f3e90e7dab38cbd93.png" style="width:0.26736in;height:1.16389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.66736in;height:0.64097in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Green LED*1</td>
<td>USB Cable*1</td>
<td>220Ω Resistor*3</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Wiring Diagram**

![](/media/a991f5cc6f8759eca3b9d01f95fe4854.png)

**Note:**

How to connect a LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω Five-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

**4. Test Code**

Codes used in this tutorial are saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
05：Traffic Lights”. and double left-click
“Project\_05\_Traffic\_Lights.py”.

![](/media/3e7a7b6c0b24bb17c40d2df0a774a6af.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>led_red = Pin(0, Pin.OUT) # create red led object from Pin 0, Set Pin 0 to output</p>
<p>led_yellow = Pin(2, Pin.OUT) # create yellow led object from Pin 2, Set Pin 2 to output</p>
<p>led_green = Pin(15, Pin.OUT) # create green led object from Pin 15, Set Pin 15 to output</p>
<p>while True:</p>
<p>led_red.value(1) # Set red led turn on</p>
<p>time.sleep(5) # Sleep 5s</p>
<p>led_red.value(0) # Set red led turn off</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_green.value(1)</p>
<p>time.sleep(5)</p>
<p>led_green.value(0)</p></td>
</tr>
</tbody>
</table>

**5.** **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/2065c1fd3ae9e84526ccf18f1f5f0cc8.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see are below:

① First, the green light will be on for five seconds and then off; 

② Next, the yellow light blinks three times and then goes off;

③ Then, the red light goes on for five seconds and then goes off;

④ Repeat steps 1 to 3 above.

Press “Ctrl+C” or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” to
exit the program.

![](/media/3b8f375f1e2f09e2f7f27b3cd4c13bc4.png)

**Project 07: Flowing Water Light**

1.  **Introduction**

In our daily life, we can see many billboards composed of different
colors of LED. They constantly change the light (like water) to attract
customers' attention. In this project, we will use ESP32 to control 10
leds to achieve the effect of flowing water.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:2.17847in;height:1.0625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.95208in;height:2.33472in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7eb361d680dfa351f07f8527aeb37abd.png" style="width:0.275in;height:1.17361in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.66736in;height:0.64097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Red LED*1</td>
<td>220Ω Resistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Wiring Diagram**

![](/media/548f889607bdb0ce017c58f323c85dfa.png)

**Note:**

How to connect a LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω Five-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

4.  **Test Code**

This project is designed to make a flowing water lamp. Actions: First
turn LED \#1 on, then turn it off. Then turn LED \#2 on, and then turn
it off... and repeat the same to all 10 LEDs until the last LED turns
off. This process is repeated to achieve the“movements”of flowing water.

Codes used in this tutorial are saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
07：Flowing Water Light”, and double left-click
“Project\_07\_Flowing\_Water\_Light.py”.

![](/media/67c86d2d042de2cc00093ca0b608bec5.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Use an array to define 10 GPIO ports connected to LED Bar Graph for easier operation.</p>
<p>pins = [22, 21, 19, 18, 17, 16, 4, 0, 2, 15]</p>
<p>#Use two for loops to turn on LEDs separately from left to right and then back from right to left</p>
<p>def showLed():</p>
<p>for pin in pins:</p>
<p>print(pin)</p>
<p>led = Pin(pin, Pin.OUT)</p>
<p>led.value(1)</p>
<p>time.sleep_ms(100)</p>
<p>led.value(0)</p>
<p>time.sleep_ms(100)</p>
<p>for pin in reversed(pins):</p>
<p>print(pin)</p>
<p>led = Pin(pin, Pin.OUT)</p>
<p>led.value(1)</p>
<p>time.sleep_ms(100)</p>
<p>led.value(0)</p>
<p>time.sleep_ms(100)</p>
<p>while True:</p>
<p>showLed()</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/d6dc066d1004176c398b7c7b1588836a.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that 10 LEDs will light up from left to right
and then back from right to left. Press“Ctrl+C” or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” to exit the program.

![](/media/9ccd5984375ca74cf3949e0042db25c6.png)

![](/media/912e2c3f88b522b89b9935548bae3bd9.png)

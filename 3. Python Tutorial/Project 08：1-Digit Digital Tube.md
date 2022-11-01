**Project 08：1-Digit Digital Tube**

1.  **Introduction**

The 1-Digit 7-Segment display is an device that displays decimal
numbers, which is widely used in digital clocks, electronic meters,
basic calculators and other electronic devices that display digital
information. In this project, we will use ESP32 to control 1-Digit
7-segment display to display numbers.

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
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/f52aeaa1de53c2e89338b2f42da4b029.png" style="width:0.52847in;height:0.58958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.66736in;height:0.64097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>1-Digit 7-Segment Display*1</td>
<td>220Ω Resistor*8</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

**3. Component Knowledge**

![](/media/e44a0f27beec739ee13e68c04865989f.png)

**1-Digit 7-Segment Display:** It is a semiconductor light emitting
device, and its basic unit is a light-emitting diode (LED). The digital
tube display can be divided into 7-segment display and 8-segment display
according to the number of segments.

The 8-segment display has one more LED unit than the 7-segment display
(used for decimal point display). Each segment of the 7-segment display
is a separate LED. According to the connection mode of the LED unit, the
digital tube can be divided into a common anode digital tube and a
common cathode digital tube.

In the common cathode 7-segment display, all the cathodes (or negative
pole) of the segmented LEDs are connected together, so you should
connect the common cathode to GND. If you are about to light up a
segmented LED, you can set its associated pin to“HIGH”.

In the common anode 7-segment display, the LED anodes (positive pole) of
all segments are connected together, so you should connect the common
anode to“+5V”. If you are about to light up a segmented LED, you can set
its associated pin to“LOW”.

![](/media/28fd057848fbe0e8c8e3362768e7aa44.png)

Each part of the digital tube is composed of an LED. So when you use it,
you also need to use a current limiting resistor. Otherwise, the LED
will be damaged. In this experiment, we will use an ordinary common
cathode one-digit digital tube. As we mentioned above, you should
connect the common cathode to GND. If you are about to light up a
segmented LED, you can set its associated pin to“HIGH”.

**4.****Wiring Diagram**

Note:The direction of the 7-segment display inserted into the breadboard
is consistent with the wiring diagram, with one more point in the lower
right corner.

![](/media/631ee0861da60ed02d191de0e0e210d9.png)

![](/media/5f01d1eea2bb207f19dee4f437f93bc8.png)

5.  **Test Code**

The digital display is divided into 7 segments, and the decimal point
display is divided into 1 segment. When certain numbers are displayed,
the corresponding segment will be lit. For example, when the number 1 is
displayed, segments b and c will be turned on.

Codes used in this tutorial are saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
08：1-Digit Digital Tube”, and double left-click
“Project\_08\_One\_Digit\_Digital\_Tube.py”.

![](/media/3be7059c709f19115166838408aee85f.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>a = Pin(16, Pin.OUT)</p>
<p>b = Pin(4, Pin.OUT)</p>
<p>c = Pin(5, Pin.OUT)</p>
<p>d = Pin(18, Pin.OUT)</p>
<p>e = Pin(19, Pin.OUT)</p>
<p>f = Pin(22, Pin.OUT)</p>
<p>g = Pin(23, Pin.OUT)</p>
<p>dp = Pin(17, Pin.OUT)</p>
<p>pins = [Pin(id,Pin.OUT) for id in [16, 4, 5, 18, 19, 22, 23, 17]]</p>
<p>def show(code):</p>
<p>for i in range(0, 8):</p>
<p>pins[i].value(~code &amp; 1)</p>
<p>code = code &gt;&gt; 1</p>
<p>#Select code from 0 to 9</p>
<p>mask_digits = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8,0x80, 0x90]</p>
<p>for code in reversed(mask_digits):</p>
<p>show(code)</p>
<p>time.sleep(1)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/7be4c73143be588035ba0e6d0e1c6fe4.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the 1-Digit 7-Segment Display will display
numbers from 9 to 0. Press “Ctrl+C” or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” to exit the
program.

![](/media/c84378a13a1f9b578d8edb57baaafd47.png)

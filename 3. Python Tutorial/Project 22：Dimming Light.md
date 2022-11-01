**Project 22：Dimming Light**

1.  **Introduction**

A potentiometer is a three-terminal resistor with sliding or rotating
contacts that forms an adjustable voltage divider. It works by changing
the position of the sliding contacts across a uniform resistance. In the
potentiometer, the entire input voltage is applied across the whole
length of the resistor, and the output voltage is the voltage drop
between the fixed and sliding contact.

In this project, we will learn how to use ESP32 to read the values of
the potentiometer, and make a dimming lamp with LED.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:1.74861in;height:0.85347in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.64028in;height:1.56944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/03ab81e8b4f09287d2781ef0fd297f85.png" style="width:0.70556in;height:1.08125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a3acf081c77644a721e572c18772b36e.png" style="width:0.23819in;height:1.01667in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Potentiometer*1</td>
<td>Red LED*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:0.25833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td></td>
</tr>
<tr class="even">
<td>220ΩResistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/03ab81e8b4f09287d2781ef0fd297f85.png)

**Adjustable potentiometer:** It is a kind of resistor and an analog
electronic component, which has two states of 0 and 1(high level and low
level). The analog quantity is different, its data state presents a
linear state such as 1 \~ 1024。

**ADC :** An ADC is an electronic integrated circuit used to convert
analog signals such as voltages to digital or binary form consisting of
1s and 0s. The range of our ADC on ESP32 is 12 bits, that means the
resolution is 2^12=4096, and it represents a range (at 3.3V) will be
divided equally to 4096 parts. The rage of analog values corresponds to
ADC values. So the more bits the ADC has, the denser the partition of
analog will be and the greater the precision of the resulting
conversion.

![](/media/f6c45550f4adf8373d7f1d01daec2c64.png)

Subsection 1: the analog in rang of 0V---3.3/4095 V corresponds to
digital 0;

Subsection 2: the analog in rang of 3.3/4095 V---2\*3.3 /4095V
corresponds to digital 1;

…

The following analog will be divided accordingly.

The conversion formula is as follows:

**DAC：**The reversing of this process requires a DAC, Digital-to-Analog
Converter. The digital I/O port can output high level and low level (0
or 1), but cannot output an intermediate voltage value.

This is where a DAC is useful. ESP32 has two DAC output pins with 8-bit
accuracy, GPIO25 and GPIO26, which can divide VCC (here is 3.3V) into
2^8=256 parts. For example, when the digital quantity is 1, the output
voltage value is 3.3/256 \*1 V, and when the digital quantity is 128,
the output voltage value is 3.3/256 \*128=1.65V, the higher the accuracy
of DAC, the higher the accuracy of output voltage value will be.

The conversion formula is as follows:

**ADC on ESP32：**

ESP32 has 16 pins can be used to measure analog signals. GPIO pin
sequence number and analog pin definition are shown in the following
table：

<table>
<tbody>
<tr class="odd">
<td><strong>ADC number in ESP32</strong></td>
<td><strong>ESP32 GPIO number</strong></td>
</tr>
<tr class="even">
<td><strong>ADC0</strong></td>
<td><strong>GPIO 36</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC3</strong></td>
<td><strong>GPIO 39</strong></td>
</tr>
<tr class="even">
<td><strong>ADC4</strong></td>
<td><strong>GPIO 32</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC5</strong></td>
<td><strong>GPIO33</strong></td>
</tr>
<tr class="even">
<td><strong>ADC6</strong></td>
<td><strong>GPIO34</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC7</strong></td>
<td><strong>GPIO 35</strong></td>
</tr>
<tr class="even">
<td><strong>ADC10</strong></td>
<td><strong>GPIO 4</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC11</strong></td>
<td><strong>GPIO0</strong></td>
</tr>
<tr class="even">
<td><strong>ADC12</strong></td>
<td><strong>GPIO2</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC13</strong></td>
<td><strong>GPIO15</strong></td>
</tr>
<tr class="even">
<td><strong>ADC14</strong></td>
<td><strong>GPIO13</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC15</strong></td>
<td><strong>GPIO 12</strong></td>
</tr>
<tr class="even">
<td><strong>ADC16</strong></td>
<td><strong>GPIO 14</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC17</strong></td>
<td><strong>GPIO27</strong></td>
</tr>
<tr class="even">
<td><strong>ADC18</strong></td>
<td><strong>GPIO25</strong></td>
</tr>
<tr class="odd">
<td><strong>ADC19</strong></td>
<td><strong>GPIO26</strong></td>
</tr>
</tbody>
</table>

**DAC on ESP32：**

ESP32 has two 8-bit digital analog converters to be connected to GPIO25
and GPIO26 pins, respectively, and it is immutable. As shown in the
following table：

<table>
<tbody>
<tr class="odd">
<td><strong>Simulate pin number</strong></td>
<td><strong>GPIO number</strong></td>
</tr>
<tr class="even">
<td><strong>DAC1</strong></td>
<td><strong>GPIO25</strong></td>
</tr>
<tr class="odd">
<td><strong>DAC2</strong></td>
<td><strong>GPIO26</strong></td>
</tr>
</tbody>
</table>

4.  **Read the values of the potentiometer**

We connect the potentiometer to the analog IO port of ESP32 to read the
ADC value, DAC value and voltage value of the potentiometer, please
refer to the wiring diagram below：

![](/media/0cda3256a0930404abc097ec8ffa3013.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
22：Dimming Light”，and then double
left-click“Project\_22.2\_Dimming\_Light.py”.

![](/media/06ac796108af1e3f93eb1cea8519421e.png)

<table>
<tbody>
<tr class="odd">
<td><p># Import Pin, ADC and DAC modules.</p>
<p>from machine import ADC,Pin,DAC</p>
<p>import time</p>
<p># Turn on and configure the ADC with the range of 0-3.3V</p>
<p>adc=ADC(Pin(36))</p>
<p>adc.atten(ADC.ATTN_11DB)</p>
<p>adc.width(ADC.WIDTH_12BIT)</p>
<p># Read ADC value once every 0.1seconds, convert ADC value to DAC value and output it,</p>
<p># and print these data to “Shell”.</p>
<p>try:</p>
<p>while True:</p>
<p>adcVal=adc.read()</p>
<p>dacVal=adcVal//16</p>
<p>voltage = adcVal / 4095.0 * 3.3</p>
<p>print("ADC Val:",adcVal,"DACVal:",dacVal,"Voltage:",voltage,"V")</p>
<p>time.sleep(0.1)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/0cd6434f99036eae34e08cf41e077e02.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the "Shell" window under Thonny IDE will
print out the ADC value, DAC value and voltage value of the
potentiometer. When the potentiometer handle is turned, the values will
change. Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart
backend”to exit the program.

![](/media/ec206f4a6e39e73ca1090463b0fed249.png)

![](/media/65e6848785b8e09c731df4dd1f68a3a0.png)

5.  **Wiring diagram of the dimming lamp**

In the previous step, we read the ADC value, DAC value and voltage value
of the potentiometer. Now we need to convert the ADC value of the
potentiometer into the brightness of the LED to make a lamp that can
adjust the brightness.The wiring diagram is as follow:

![](/media/3396bd77169711de6e15da73f14c8afb.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
22：Dimming Light”，and then double
left-click“Project\_22.2\_Dimming\_Light.py”.

![](/media/38a314cdea1135d7b329ffd722ef2946.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,PWM,ADC</p>
<p>import time</p>
<p>pwm =PWM(Pin(15,Pin.OUT),1000)</p>
<p>adc=ADC(Pin(36))</p>
<p>adc.atten(ADC.ATTN_11DB)</p>
<p>adc.width(ADC.WIDTH_10BIT)</p>
<p>try:</p>
<p>while True:</p>
<p>adcValue=adc.read()</p>
<p>pwm.duty(adcValue)</p>
<p>print(adc.read())</p>
<p>time.sleep_ms(100)</p>
<p>except:</p>
<p>pwm.deinit()</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/044b76a8bd7db21d2d7181fd6278d3cb.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that turn the potentiometer handle and the
brightness of the LED will change accordingly. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/bf01f65e47f89542d2d8d4c52410d74d.png)

![](/media/eca30dead3f4923afa0dcb0306db2319.jpeg)

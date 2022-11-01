**Project 23：Flame Alarm**

1.  **Introduction**

Fire is a terrible disaster and fire alarm systems are very useful in
houses、commercial buildings and factories. In this project, we will use
ESP32 to control a flame sensor, a buzzer and a LED to simulate fire
alarm devices. This is a meaningful maker activity.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/df7fdb857f6490486514896b60cabe10.jpeg" style="width:1.39722in;height:0.68264in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.55208in;height:1.35417in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/ef77f5a64c382157fc2dea21ec373fef.png" style="width:0.29514in;height:1.25903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:0.86111in;height:0.70069in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Red LED*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a50ec3e38adf10643eafac8cb62bec8a.png" style="width:0.20278in;height:1.25764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:0.25833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/b395b1cd2678f87b3a34dec15659efbc.png" style="width:0.22431in;height:1.00556in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
</tr>
<tr class="even">
<td>Flame Sensor*1</td>
<td>220ΩResistor*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/9197d4aff9356c585b7ef68e33a6881d.png" style="width:0.27986in;height:1.08819in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td></td>
</tr>
<tr class="even">
<td>NPN Transistor(S8050)*1</td>
<td>1kΩ Resistor*1</td>
<td>USB Cable*1</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/a50ec3e38adf10643eafac8cb62bec8a.png)

The flame emits a certain amount IR light that is invisible to the human
eye, but our flame sensor can detect it and alert a microcontroller
(such as ESP32) that a fire has been detected. It has a specially
designed infrared receiver tube to detect the flame and then convert the
flame brightness into a fluctuating level signal. 

The short pin of the receiving triode is negative pole and the other
long pin is positive pole. We should connect the short pin (negative) to
5V and the long pin (positive) to the analog pin, a resistor and GND. As
shown in the figure below：

![](/media/87bd204db523c602c80745266c1ee452.png)

**Note:** Since vulnerable to radio frequency radiation and temperature
changes, the flame sensor should be kept away from heat sources like
radiators, heaters and air conditioners, as well as direct irradiation
of sunlight, headlights and incandescent light.

4.  **Read the values of the flame sensor**

We first use a simple code to read the ADC value, DAC value and voltage
value of the flame sensor and print them out. Please refer to the wiring
diagram below：

![](/media/76ce57355da1df27e049bdc6e19f0650.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
23：Flame Alarm”, and then double left-click
“Project\_23.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](/media/b4ab4d56badbead366bed085d382f224.png)

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

![](/media/c2ec0600962bd87b24376fc0986183c4.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the ”Shell” window will print out the ADC
value, DAC value and voltage value of the flame sensor. When the sensor
is closed to fire, the ADC value,DAC value and voltage value will get
greater. Conversely, they will decrease. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/8cfd1510ef6c947201dd14ff0f5ade21.png)

![](/media/65e6848785b8e09c731df4dd1f68a3a0.png)

5.  **Wiring diagram of the flame alarm**

Next, we will use a flame sensor, a buzzer, and a LED to make an
interesting project, that is flame alarm. When flame is detected, the
LED flashes and the buzzer alarms.

![](/media/e9fa0e50df23c1f2e58fdd319ad21b4c.png)

6.  **Test Code**（Note：![](/media/40a3ea572836945268b22dfc0cce29c3.png) the threshold of 500 in
    the code can be reset as required）

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
23：Flame Alarm”, and then double left-click
“Project\_23.2\_Flame\_Alarm.py”.

![](/media/08b1420f2793b1c20200af63ce5111ba.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Turn on and configure the ADC with the range of 0-3.3V</p>
<p>adc=ADC(Pin(36))</p>
<p>adc.atten(ADC.ATTN_11DB)</p>
<p>adc.width(ADC.WIDTH_12BIT)</p>
<p># create LED object from Pin 15,Set Pin 15 to output</p>
<p>led = Pin(15, Pin.OUT)</p>
<p># create buzzer object from Pin 4, Set Pin 4 to output</p>
<p>buzzer = Pin(4, Pin.OUT)</p>
<p># If the flame sensor detects a flame, the buzzer will beep</p>
<p># and the LED will blink when the analog value is greater than 500</p>
<p># Otherwise, the buzzer does not sound and the LED goes off</p>
<p>while True:</p>
<p>adcVal=adc.read()</p>
<p>if adcVal &gt;500:</p>
<p>buzzer.value(1) # Set buzzer turn on</p>
<p>led.value(1) # Set led turn on</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>buzzer.value(0)</p>
<p>led.value(0) # Set led turn off</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>else:</p>
<p>buzzer.value(0) # Set buzzer turn off</p>
<p>led.value(0) # Set led turn off</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/16f7214c93439af62ac8d2a005b398ea.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that when the flame sensor detects the flame,
the LED flashes and the buzzer alarms. Otherwise, the LED does not
light, the buzzer does not sound. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/a13d1483a5d9bca9258d760f3dbb4ac8.png)

## Project 04: Breathing Led

1.  **Introduction**

A“breathing LED”is a phenomenon where an LED's brightness smoothly
changes from dark to bright and back to dark, continuing to do so and
giving the illusion of an LED“breathing. However, how to control LED’s
brightness? We need to take advantage of PWM.

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
<td>Jumper Wire*2</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

**3.** **Component Knowledge**

![](/media/6549bdbfd4e7b6b2b341012105d655e8.png)

**Analog & Digital**

Analog signal are continuous signals in both time and value. On the
contrary, a digital signal or discrete time signal is a time series
consisting of a sequence of quantities. Most signals in life are analog
signals. A familiar example of an analog signal would be how the
temperature throughout the day continuously changes and could not change
instantaneously from 0℃ to 10℃.

However, digital signals can instantaneously change in value. This
change is expressed in numbers as 1 and 0 (the basis of binary code).
Their differences can be seen more easily when compared, as shown below:

![](/media/4bdf6127e563b453a1fd8953b4ebb277.png)

In practical application, we often use binary as the digital signal,
that is a series of 0’s and 1’s. Since a binary signal only has two
values (0 or 1), it has great stability and reliability. Lastly, both
analog and digital signals can be converted into each other.

**PWM：**

PWM, Pulse-Width Modulation, is a very effective method for using
digital signals to control analog circuits. Common processors cannot
directly output analog signals. PWM technology makes it very convenient
to achieve this conversion (translation of digital to analog signals).

PWM technology uses digital pins to send certain frequencies of square
waves, that is, the output of high levels and low levels, which
alternately last for a while. The total time for each set of high levels
and low levels is generally fixed, which is called the period (Note: the
reciprocal of the period is frequency). The time of high level outputs
is generally called “pulse width”, and the duty cycle is the percentage
of pulse width (PW) to the total period (T) of the waveform.

The longer the output of high levels last, the longer the duty cycle and
the higher the corresponding voltage in the analog signal will be. The
following figures show how the analog signal voltages vary between
0V-3.3V(high level is 3.3V) corresponding to the pulse width 0%-100%:

![](/media/a439e1bd8a4578b43b7188c821d58594.jpeg)

The longer the PWM duty cycle is, the higher the output power will be.
Therefore, we can use PWM to control the brightness of an LED or the
speed of DC motor and so on. It is evident from the above that PWM is
not real analog, and the effective value of the voltage is equivalent to
the corresponding analog. Then we can control the output power of the
LED and other output modules to achieve different effects.

**ESP32 and PWM**

Almost all ESP32 input/output pins are available for PWM (pulse width
modulation).  These pins can be used to control motors, LED lights and
colors, etc. 

**4.** **Wiring Diagram**

![](/media/0735997593c8858ad6441d8e9867206f.png)

**Note:**

How to connect a LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω Five-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

5.  **Test Code**

The GPIO15 outputs PWM, and the pulse width gradually increases from 0%
to 100%, and then gradually decreases from 100% to 0%.

Codes used in this tutorial are saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
04：Breathing Led”, and double left-click
“Project\_04\_Breathing\_LED.py”.

![](/media/36ed8d4dadbfa227747fb2a2040c1fe6.png)

<table>
<tbody>
<tr class="odd">
<td><p>import time</p>
<p>from machine import Pin,PWM</p>
<p>#The way that the ESP32 PWM pins output is different from traditionally controllers.</p>
<p>#It can change frequency and duty cycle by configuring PWM’s parameters at the initialization stage.</p>
<p>#Define GPIO15’s output frequency as 10000Hz and its duty cycle as 0, and assign them to PWM.</p>
<p>pwm =PWM(Pin(15,Pin.OUT),10000,0)</p>
<p>try:</p>
<p>while True:</p>
<p>#The range of duty cycle is 0-1023, so we use the first for loop to control PWM to change the duty</p>
<p>#cycle value,making PWM output 0% -100%; Use the second for loop to make PWM output 100%-0%.</p>
<p>for i in range(0,1023):</p>
<p>pwm.duty(i)</p>
<p>time.sleep_ms(1)</p>
<p>for i in range(0,1023):</p>
<p>pwm.duty(1023-i)</p>
<p>time.sleep_ms(1)</p>
<p>except:</p>
<p>#Each time PWM is used, the hardware Timer will be turned ON to cooperate it. Therefore, after each use of PWM,</p>
<p>#deinit() needs to be called to turned OFF the timer. Otherwise, the PWM may fail to work next time.</p>
<p>pwm.deinit()</p></td>
</tr>
</tbody>
</table>

**6. Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/89485986d9a0a7c5efcfd4b0356440f5.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the LED will change from bright to dim then
from dim to bright gradually like breathing. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” to exit the program.

![](/media/62c772c3c9dadbfc1b3b720dab647f8e.png)

![](/media/3673c95868f245ee28365de8e51d2ced.png)

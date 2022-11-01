**Project 18：Small Fan**

1.  **Introduction**

In hot summer, we need electric fans to cool us down, so in this
project, we will use a ESP32 to control a DC motor and small fan blades
to make a small electric fan.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:2.17847in;height:1.0625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.94722in;height:2.32014in" /></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/5fe5f8cd6e75e7f8d4ec71f54a4ac2f5.png" style="width:0.87292in;height:0.37083in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/5eba8bae9e1d18b959ca425a9cc83fd2.jpeg" style="width:1.07569in;height:0.43472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/655e6c465cb423279e0908513a983711.png" style="width:0.85694in;height:0.75347in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/df3db6765ee8c86beafa8410e87dd50d.png" style="width:0.77361in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>L293D Chip*1</td>
<td>DC Motor*1</td>
<td>Fan*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/b65d826ca481982fed0212dba2957c7c.jpeg" style="width:1.57361in;height:1.13611in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/6734084c96238569a513a5ff3190621d.png" style="width:1.15486in;height:0.49861in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a815c48437199c6ab79d74cd2d583de0.png" style="width:0.24722in;height:1.14097in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Battery Holder*1</td>
<td>Keyestudio Breadboard special power module*1</td>
<td>No.5 Battery (self-provided)*6</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/5fe5f8cd6e75e7f8d4ec71f54a4ac2f5.png)

**L293D Chip:** The L293D is a DC motor driver IC that can be used to
drive dc motors or stepper motors in some robotics projects.  It has 16
pins and can drive 2-channel DC motors at the same time.  Its input
voltage range is 4.5V \~ 36V, and each channel output current is MAX
600mA, which can drive the inductive load, especially its input terminal
can be directly connected with the single chip microcomputer.

Therefore, it is very convenient to be controlled by the single chip
microcomputer.  When driving a small DC motor, 2-channel motors can be
directly controlled, and the motor can be positive and reverse.

In order to achieve this function we solely need to change the input
high and low level. There are many motor driver boards of L293D chips in
the market, of course, we can also use them through simple connection. 

**Diagram of the L293D pins**

![](/media/2e5e0bd5b4577ac159d0568404dc21b5.png)

<table>
<tbody>
<tr class="odd">
<td>#</td>
<td>Name</td>
<td>Description</td>
</tr>
<tr class="even">
<td>1</td>
<td>Enable1</td>
<td>Input 1(2) and 2(7)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>In1</td>
<td>Control output pin1</td>
</tr>
<tr class="even">
<td>3</td>
<td>Out1</td>
<td>Connect to one end of motor 1</td>
</tr>
<tr class="odd">
<td>4</td>
<td>0V</td>
<td>Connect to grounding (0V) of the circuit</td>
</tr>
<tr class="even">
<td>5</td>
<td>0V</td>
<td>Connect to grounding (0V) of the circuit</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Out2</td>
<td>Connect to the other end of motor 1</td>
</tr>
<tr class="even">
<td>7</td>
<td>In2</td>
<td>Control output pin2</td>
</tr>
<tr class="odd">
<td>8</td>
<td>+V motor</td>
<td>Connect to the voltage pins of the running motor(4.5V to 36V)</td>
</tr>
<tr class="even">
<td>9</td>
<td>Enable2</td>
<td>Input 3(10) and 4(15)</td>
</tr>
<tr class="odd">
<td>10</td>
<td>In3</td>
<td>Control output pin3</td>
</tr>
<tr class="even">
<td>11</td>
<td>Out3</td>
<td>Connect to one end of motor 2</td>
</tr>
<tr class="odd">
<td>12</td>
<td>0V</td>
<td>Connect to grounding (0V) of the circuit</td>
</tr>
<tr class="even">
<td>13</td>
<td>0V</td>
<td>Connect to grounding (0V) of the circuit</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Out4</td>
<td>Connect to the other end of motor 2</td>
</tr>
<tr class="even">
<td>15</td>
<td>In4</td>
<td>Control output pin4</td>
</tr>
<tr class="odd">
<td>16</td>
<td>+V</td>
<td>Connect to+ 5V to enable IC function</td>
</tr>
</tbody>
</table>

**Keyestudio Breadboard Power Supply Module**

![](/media/7ff03f4506988f1ce99c5757892fc6de.jpeg)

**Introduction**

This breadboard power supply module is compatible with 5V and 3.3V,
which can be applied to MB102 breadboard. The module contains two
channels of independent control, powered by the USB all the way.

The output voltage is constant for the DC5V, and another way is powered
by DC 7-12V, output controlled by the slide switch, respectively for
DC5V and DC3.3V.

If the other power supply is DC 7-12v, when the slide switch is switched
to +5V, the output voltages of the left and right lines of the module
are DC 5V. When the slide switch is switched to +3V, the output voltage
of the USB power supply terminal of the module is DC5V , and the output
voltage of the DC 7-12V power supply terminal of the other power supply
is DC3.3V.

**Specification**

  - Applied to MB102 breadboard

  - Input voltage：DC 7-12V or powered by USB

  - Output voltage：3.3V or 5V

  - Max output current：\<700mA

  - Up and down two channels of independent control, one of which can be
    switched to 3.3V or 5V

Comes with two sets of DC output pins, easy for external use

4.  **Wiring Diagram**
    
    ![](/media/b7a0a9defecdb20f2d070aa9920dfe69.png)

(Note: Connect the wirings and then install a small fan blade on the DC
motor. )

5.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
18：Small Fan”, and then double left-click“Project\_18\_
Small\_Fan.py”.

![](/media/9a65851a625a3d7691d399f6d0899a3e.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,PWM</p>
<p>import time</p>
<p>#Pin of each section of L293D and set as output</p>
<p>IN1_Pin = 2</p>
<p>IN2_Pin = 15</p>
<p>ENA_Pin = 0 #Control the speed of the motor</p>
<p># speed：speed，0-100</p>
<p># direction: Rotation direction,1 is clockwise,0 stops,-1 counterclockwise</p>
<p># speed_pin：Pin number that controls the start and stop of the motor</p>
<p>def motorRun(speed, direction, speed_pin, clockwise_pin, anti_clockwise_pin):</p>
<p>if speed &gt; 100: speed=100</p>
<p>if speed &lt; 0: speed=0</p>
<p>in1 = Pin(anti_clockwise_pin, Pin.OUT)</p>
<p>in2 = Pin(clockwise_pin, Pin.OUT)</p>
<p>pwm = PWM(Pin(speed_pin))</p>
<p>pwm.freq(50)</p>
<p>pwm.duty(int(speed/100*4096))</p>
<p>if direction &lt; 0:</p>
<p>in2.value(0)</p>
<p>in1.value(1)</p>
<p>if direction == 0:</p>
<p>in2.value(0)</p>
<p>in1.value(0)</p>
<p>if direction &gt; 0:</p>
<p>in2.value(1)</p>
<p>in1.value(0)</p>
<p>while True:</p>
<p>motorRun(100, 1, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(5)</p>
<p>motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(2)</p>
<p>motorRun(100, -1, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(5)</p>
<p>motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(2)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/a06eb0e5e95fe3dd011e7109aac87552.png)

Power the external power supply and power on.
Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the small fan turns counterclockwise for 5
seconds and stops for 2 seconds, and then turns clockwise for 5 seconds
and stops for 2 seconds. Repeat this rule for 5 times and then the small
fan stops. Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart
backend”to exit the program.

![](/media/66844471ea8c40db6444c2c3853c7f1f.png)

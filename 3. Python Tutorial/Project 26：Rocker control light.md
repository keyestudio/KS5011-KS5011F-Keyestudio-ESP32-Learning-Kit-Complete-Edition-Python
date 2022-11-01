**Project 26：Rocker control light**

1.  **Introduction**

The rocker module is a component with two analog inputs and one digital
input. It is widely used in areas such as game operation、robot control
and drone control.

In this project, we will use a ESP32 and a joystick module to control
RGB, so that you can have a deeper understanding of the principle and
operation of the joystick module in practice. 

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:1.59722in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.75972in;height:1.8625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/d087b123748cbfb8ed9f517150db71c5.png" style="width:1.71042in;height:0.95139in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Joystick Module*1</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/af749ecbde89c728a8c63e6527781cac.png" style="width:0.16806in;height:0.93194in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.92778in;height:0.89167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.14167in;height:0.61111in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/f1aed48e2c02214415853ad2358f3744.png" style="width:1.21875in;height:1.02986in" /></td>
</tr>
<tr class="even">
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td>M-F Dupont Wires</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
        ![](/media/d087b123748cbfb8ed9f517150db71c5.png)

**Joystick** **module:** It mainly uses PS2 joystick components. In
fact, the joystick module has 3 signal terminal pins, which simulate a
three-dimensional space. The pins of the joystick module are GND, VCC,
and signal terminals (B, X, Y).

The signal terminals X and Y simulate the X-axis and Y-axis of the
space. When controlling, the X and Y signal terminals of the module are
connected to the analog port of the microcontroller. The signal terminal
B simulates the Z axis of the space, it is generally connected to the
digital port and used as a button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V),
GND is connected to the microcontroller GND, the voltage in the original
state is about 1.65V or 2.5V. In the X-axis direction, when moving in
the direction of the arrow, the voltage value increases, and the maximum
voltage can be reached. Moving in the opposite direction of the arrow,
the voltage value gradually decreases to the minimum voltage.

In the Y-axis direction, the voltage value decreases gradually as it
moves in the direction of the arrow on the module, decreasing to the
minimum voltage. As the arrow is moved in the opposite direction, the
voltage value increases and can reach the maximum voltage. In the Z-axis
direction, the signal terminal B is connected to the digital port and
outputs 0 in the original state and outputs 1 when pressed.

In this way, we can read the two analog values and the high and low
level conditions of the digital port to determine the operating status
of the joystick on the module.

**Features:**

Input voltage：DC 3.3V \~ 5V

Output signal：X/Y dual axis analog value +Z axis digital signal

[Range](javascript:;) [of](javascript:;) [application](javascript:;)：Suitable
for control point coordinate movement in plane as well as control of two
degrees of freedom steering gear, etc.  

[Product](javascript:;) [feature](javascript:;)s：Exquisite appearance,
joystick feels superior, simple operation, sensitive response, long
service life.

4.  **Read the value of the Joystick Module**

We must use ESP32’s analog IO ports to read the value from the X/Y pin
of the Joystick module and use the digital IO ports to read the digital
signal of the button. Please connect the wires according to the wiring
diagram below：

![](/media/b611755eacc4c603e6c0555aced929cb.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
26：Rocker control light”, and then double left-click
“Project\_26.1\_Read\_Rocker\_Value.py”.

![](/media/5e7922ce13ac55820321f90a97172e6f.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC</p>
<p>import time</p>
<p># Initialize the joystick module (ADC function)</p>
<p>rocker_x=ADC(Pin(36))</p>
<p>rocker_y=ADC(Pin(39))</p>
<p>button_z=Pin(14,Pin.IN,Pin.PULL_UP)</p>
<p># Set the acquisition range of voltage of the two ADC channels to 0-3.3V,</p>
<p># and the acquisition width of data to 0-4095.</p>
<p>rocker_x.atten(ADC.ATTN_11DB)</p>
<p>rocker_y.atten(ADC.ATTN_11DB)</p>
<p>rocker_x.width(ADC.WIDTH_12BIT)</p>
<p>rocker_y.width(ADC.WIDTH_12BIT)</p>
<p># In the code, configure Z_Pin to pull-up input mode.</p>
<p># In loop(), use Read () to read the value of axes X and Y</p>
<p># and use value() to read the value of axis Z, and then display them.</p>
<p>while True:</p>
<p>print("X,Y,Z:",rocker_x.read(),",",rocker_y.read(),",",button_z.value())</p>
<p>time.sleep(0.5)</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/6f58e589994f6e0cb11b08e0536a3872.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the ”Shell” window will print out the
analog and digital values of the current joystick. Moving the joystick
or pressing it will change the analog and digital values.
Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to
exit the program.

![](/media/5374bacccc39a461935c7faee08ae1ce.png)

![](/media/06a9de681779df5cfc7e6bc24a928a3a.jpeg)

![](/media/6e7dd18099836222c5237c9e0e659539.png)

5.  **Wiring diagram of joystick controls RGB**

We just read the value of the joystick module, we need to do something
with the joystick module and RGB here, follow the diagram below for
wiring：

![](/media/4ec49b488fedf216d03e49f83bc8443a.png)

6.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
26：Rocker control light”and then double left-click
“Project\_26.2\_Rocker\_Control\_Light.py”.

![](/media/160365a2dc555d0cdd00d99ca7726c9a.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC,PWM</p>
<p>import time</p>
<p>#Set RGB light interface and frequency</p>
<p>rgb_r = PWM(Pin(4))</p>
<p>rgb_g = PWM(Pin(0))</p>
<p>rgb_b = PWM(Pin(2))</p>
<p>rgb_b.freq(1000)</p>
<p>rgb_r.freq(1000)</p>
<p>rgb_g.freq(1000)</p>
<p>#Set rocker pin</p>
<p>rocker_x=ADC(Pin(36))</p>
<p>rocker_y=ADC(Pin(39))</p>
<p># Set the acquisition range of voltage of the two ADC channels to 0-3.3V,</p>
<p># and the acquisition width of data to 0-4095.</p>
<p>rocker_x.atten(ADC.ATTN_11DB)</p>
<p>rocker_y.atten(ADC.ATTN_11DB)</p>
<p>rocker_x.width(ADC.WIDTH_12BIT)</p>
<p>rocker_y.width(ADC.WIDTH_12BIT)</p>
<p>while True:</p>
<p>y = rocker_y.read()#Get Y value of rocker</p>
<p>x = rocker_x.read()#Get X value of rocker</p>
<p>if x &lt; 1000: #left</p>
<p>rgb_b.duty(0)</p>
<p>rgb_r.duty(4095)</p>
<p>rgb_g.duty(0)</p>
<p>elif x &gt; 3000: #right</p>
<p>rgb_b.duty(0)</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(4095)</p>
<p>elif y &lt; 1000: #down</p>
<p>rgb_b.duty(4095)</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(0)</p>
<p>elif y &gt; 3000: #up</p>
<p>rgb_b.duty(4095)</p>
<p>rgb_r.duty(4095)</p>
<p>rgb_g.duty(4095)</p>
<p>time.sleep(0.01)</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/786210f9527069debff49c7de2a15ce1.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that ①If the joystick is moved to the far left
in the X direction, the RGB light turns red. ②If the joystick is moved
to the far right in the X direction, the RGB light turns green. ③If the
joystick is moved to the up in the Y direction, the RGB light turns
white. ④If the joystick is moved to the down in the Y direction, the RGB
light turns blue. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/a803e7414402b5f6aa551d9fc9b093ed.png)

![](/media/9c2d0d8777200827b16c49b752d45c4c.jpeg)

## Project 20：Stepping Motor 

1.  **Introduction**

Stepper motor is the most important part of industrial robot 3D printer
lathes and other mechanical equipment with accurate positioning. In this
project, we will use a ESP32 to control ULN2003 stepper motor driver
board to drive the stepper motor to rotate.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:1.58264in;height:0.77292in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.84236in;height:2.06319in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/6c9c142fb9187aeb8337493ca5dd5ee7.jpeg" style="width:1.56111in;height:1.03819in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>ULN2003 Stepper Motor Drive Board*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/8ebb14a35091dc8d02d95cb6748dd1e9.png" style="width:0.93403in;height:0.92431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/6ba5c3147b32861b2dbc6b9986382c1b.png" style="width:0.88681in;height:1.04722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>Stepper Motor *1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/b65d826ca481982fed0212dba2957c7c.jpeg" style="width:1.57361in;height:1.13611in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a8fe41500d5d16511fd90518f745d398.png" style="width:1.80903in;height:0.78125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a815c48437199c6ab79d74cd2d583de0.png" style="width:0.41042in;height:1.89444in" /></td>
</tr>
<tr class="even">
<td>Battery Holder*1</td>
<td>Keyestudio Breadboard special power module*1</td>
<td>No.5 battery (self-provided)*6</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
    ![](/media/8ebb14a35091dc8d02d95cb6748dd1e9.png)

**Stepper motor:** It is a motor controlled by a series of
electromagnetic coils. It can rotate by the exact number of degrees (or
steps) needed, allowing you to move it to a precise position and keep it
there. It does this by supplying power to the coil inside the motor in a
very short time, but you must always supply power to the motor to keep
it in the position you want.

There are two basic types of stepping motors, namely unipolar stepping
motor and bipolar stepping motor. In this project, we use a 28-BYJ48
unipolar stepper motor.

![](/media/bea0e202b7bfe23d1fdcdbbe996aa6da.jpeg)

**Working Principle:**

The stepper motor is mainly composed of a stator and a rotor. The stator
is fixed. As shown in the figure below, the part of the coil group A, B,
C, and D will generate a magnetic field when the coil group is
energized. The rotor is the rotating part. As follows, the middle part
of the stator, two poles are permanent magnets.

![](/media/32748e0804b1fff434181cb228b23242.png)

Single -phase four beat: At the beginning, the coils of group A are
turned on, and the poles of the rotor point at A coil. Next, the group A
coil are disconnected, and the group B coils are turned on. The rotor
will turn clockwise to the group B. Then, group B is disconnected, group
C is turned on, and the rotor is turned to group C.

After that, group C is disconnected, and group D is turned on, and the
rotor is turned to group D. Finally, group D is disconnected, group A is
turned on, and the rotor is turned to group A coils. Therefore, rotor
turns 180° and continuously rotates B-C-D-A, which means it runs a
circle (eight phase). As shown below, the rotation principle of stepper
motor is A - B - C - D - A.

Make order inverse(D - C - B - A - D .....) if you want to make stepper
motor rotate anticlockwise.

![](/media/b8ae50bbdee2dd5bc683e8c450baee6a.png)

Half-phase and eight beat: 8 beat adopts single and dual beat way，A - AB
- B - BC - C - CD - D - DA - A ...... ，rotor will rotate half phase in
this order. For example, when A coil is electrified，rotor faces to A
coil , then A and B coil are connected, on this condition, the strongest
magnetic field produced lies in the central part of AB coil, which means
rotating half-phase clockwise.

**Stepper Motor Parameters:**

The rotor rotates one circle when the stepper motor we provide rotates
32 phases and with the output shaft driven by 1:64 reduction geared set.
Therefore the rotation (a circle) of output shaft requires 32 \* 64 =
2048 phases.

The step angle of 4-beat mode of 5V and 4-phase stepper motor is 11.25.
And the step angle of 8-beat mode is 5.625, the reduction ratio is 1:64.

**ULN2003 Stepper Motor Drive Board:** It is a stepper motor driver,
which converts the weak signal into a stronger control signal to drive
the stepper motor. 

The following schematic diagram shows how to use the ULN2003 stepper
motor driver board interface to connect a unipolar stepper motor to the
pins of the ESP32, and shows how to use four TIP120 interfaces.

![](/media/6fa632d2b70e97dd55565d23ec15d245.png)

4.  **Wiring Diagram**

![](/media/6333a59ee8dd57f7ceb5eaaec8d588df.png)

5.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
20：Stepping Motor”, and then double left-click
“Project\_20\_Stepping\_Motor.py”.

![](/media/55d7812efd39259305f2f77ab30184e0.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p># Pin initialization</p>
<p>in1 = Pin(15, Pin.OUT)</p>
<p>in2 = Pin(16, Pin.OUT)</p>
<p>in3 = Pin(17, Pin.OUT)</p>
<p>in4 = Pin(18, Pin.OUT)</p>
<p># Delay time</p>
<p>delay = 1</p>
<p># The number of steps required for the motor to rotate one revolution, (about 360°), with a slight deviation</p>
<p>ROUND_VALUE = 509</p>
<p># The sequence value of the four-phase eight-beat stepper motor: A-AB-B-BC-C-CD-D-DA-A。</p>
<p>STEP_VALUE = [</p>
<p>[1, 0, 0, 0],</p>
<p>[1, 1, 0, 0],</p>
<p>[0, 1, 0, 0],</p>
<p>[0, 1, 1, 0],</p>
<p>[0, 0, 1, 0],</p>
<p>[0, 0, 1, 1],</p>
<p>[0, 0, 0, 1],</p>
<p>[1, 0, 0, 1],</p>
<p>]</p>
<p># Pin output low level</p>
<p>def reset():</p>
<p>in1(0)</p>
<p>in2(0)</p>
<p>in3(0)</p>
<p>in4(0)</p>
<p># If count is positive integers turn clockwise, if count is negative integers turn counterclockwise</p>
<p>def step_run(count):</p>
<p>direction = 1 # turn clockwise</p>
<p>if count &lt; 0:</p>
<p>direction = -1 # turn counterclockwise</p>
<p>count = -count</p>
<p>for x in range(count):</p>
<p>for bit in STEP_VALUE[::direction]:</p>
<p>in1(bit[0])</p>
<p>in2(bit[1])</p>
<p>in3(bit[2])</p>
<p>in4(bit[3])</p>
<p>time.sleep_ms(delay)</p>
<p>reset()</p>
<p># If a is positive integers turn clockwise, if a is negative integers turn counterclockwise</p>
<p>def step_angle(a):</p>
<p>step_run(int(ROUND_VALUE * a / 360))</p>
<p># Cycle: turn clockwise one circle, then counterclockwise one circle.</p>
<p>while True:</p>
<p>step_run(509)</p>
<p>step_run(-509)</p>
<p>step_angle(360)</p>
<p>step_angle(-360)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/30e1c41f07ee3bbd91887e5b1dee3216.png)

Power the external power supply and power on.
Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the four LEDs ( D1,D2,D3 ,D4) on the
ULN2003 drive module will light up. The stepper motor rotates
counterclockwise first, then clockwise, and repeat these actions in an
endless loop. Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart
backend”to exit the program.

![](/media/0e7cf462ca0c42ce5028e6eab7347824.png)

![](/media/8dc4a0547390e0108c3960c31d330ee7.png)

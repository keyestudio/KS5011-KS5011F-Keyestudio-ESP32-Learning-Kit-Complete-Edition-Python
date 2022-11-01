**Project 10：8×8 Dot-matrix Display**

1.  **Introduction**

Dot matrix display is an electronic digital display device that can
display information on machine, clocks, public transport departure
indicators and many other devices. In this project, we will use ESP32 to
control 8x8 LED dot matrix in a way that light it up.

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
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/d226a1f3c801ac78321f0692143c853e.png" style="width:1.09375in;height:1.05208in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:1.03333in;height:1.02708in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>8*8 dot matrix module*1</td>
<td>220Ω Resistor*8</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**8\*8 dot matrix module：**The 8\*8 dot matrix is composed of 64 LEDs,
including row common anode and row common cathode. Our module is row
common anode, each row has a line connecting the positive pole of the
LED, and the column is connecting the negative pole of the LED lamp, as
shown in the following figure :

![](/media/69c719a7898907ab32f089f0cbbaff13.png)

![](/media/bcfa2498367eaf9c7733da15af32eae7.png)

4.  **Wiring Diagram**
    
    ![](/media/af4d73ef798a933228f16dedc6578b8e.png)

5.  **Test Code**
    
    The code used in this tutorial is saved in“4. Python Tutorial\\2.
    Python Projects”. You can move the codes to any location. For
    example, we save the codes in Disk(D) with the path of “D:\\2.
    Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
10：8×8 Dot-matrix Display”, then double
left-click“Project\_10\_8×8\_Dot\_Matrix\_Display.py”.

![](/media/685b93c4b7aec7954751535e96529462.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Define the pin of the row and Set to output.</p>
<p>row1 = Pin(14, Pin.OUT)</p>
<p>row2 = Pin(26, Pin.OUT)</p>
<p>row3 = Pin(4, Pin.OUT)</p>
<p>row4 = Pin(27, Pin.OUT)</p>
<p>row5 = Pin(19, Pin.OUT)</p>
<p>row6 = Pin(16, Pin.OUT)</p>
<p>row7 = Pin(18, Pin.OUT)</p>
<p>row8 = Pin(17, Pin.OUT)</p>
<p>#Define the pins of the column and Set to output</p>
<p>col1 = Pin(32, Pin.OUT)</p>
<p>col2 = Pin(21, Pin.OUT)</p>
<p>col3 = Pin(22, Pin.OUT)</p>
<p>col4 = Pin(12, Pin.OUT)</p>
<p>col5 = Pin(0, Pin.OUT)</p>
<p>col6 = Pin(13, Pin.OUT)</p>
<p>col7 = Pin(33, Pin.OUT)</p>
<p>col8 = Pin(25, Pin.OUT)</p>
<p>#Sets the pin of the column to low level</p>
<p>col1.value(0)</p>
<p>col2.value(0)</p>
<p>col3.value(0)</p>
<p>col4.value(0)</p>
<p>col5.value(0)</p>
<p>col6.value(0)</p>
<p>col7.value(0)</p>
<p>col8.value(0)</p>
<p>#Since the column of the lattice has been set to low level,</p>
<p>#the corresponding row of the lattice will light up when the pin of the row is at high level</p>
<p>def Row(d):</p>
<p>if(d ==1):</p>
<p>row1.value(1) #Light the first line</p>
<p>if(d ==2):</p>
<p>row2.value(1) #Light the second line</p>
<p>if(d ==3):</p>
<p>row3.value(1)</p>
<p>if(d ==4):</p>
<p>row4.value(1)</p>
<p>if(d ==5):</p>
<p>row5.value(1)</p>
<p>if(d ==6):</p>
<p>row6.value(1)</p>
<p>if(d ==7):</p>
<p>row7.value(1)</p>
<p>if(d ==8):</p>
<p>row8.value(1)</p>
<p>#Close the lattice</p>
<p>def off():</p>
<p>row1.value(0)</p>
<p>row2.value(0)</p>
<p>row3.value(0)</p>
<p>row4.value(0)</p>
<p>row5.value(0)</p>
<p>row6.value(0)</p>
<p>row7.value(0)</p>
<p>row8.value(0)</p>
<p>try:</p>
<p>print("test...")</p>
<p>while True:</p>
<p>for num in range(1,10): #Light the lattice line by line</p>
<p>Row(num)</p>
<p>if(num == 9): #Because the lattice has only 8 rows, and I'm limiting it here, is equal to 9</p>
<p>off() #Close the lattice</p>
<p>time.sleep(0.2)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/d86927974ad8ea2689a5349d46b30613.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the 8\*8 dot matrix gradually lights up.
Press“Ctrl+C” or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to
exit the program.

![](/media/689969cd82574c5ca7c8ea40ca67e390.png)

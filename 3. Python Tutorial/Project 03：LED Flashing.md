## Project 03：LED Flashing 

1.  **Introduction**

In this project, we will show you the LED flashing effect. We will work
to use the ESP32's digital pins to turn on the LED and make it flash.

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

3.  **Wiring Diagram**

First, disconnect all power supplies from the ESP32. Then build the
circuit according to the wiring diagram. After the circuit is built and
verified correctly, connect the ESP32 to your computer via a USB cable.

**Note:** Avoid any possible short circuits (especially connecting 3.3V
and GND)\!

**Warning:** The short circuit can cause high current in the circuit and
create excessive component heat and permanent damage to your hardware.

![](/media/0735997593c8858ad6441d8e9867206f.png)

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

Code running online:

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
03：LED Flashing”.

![](/media/aed4325f483f54272aba116d9d92190e.png)

Expand folder“Project 03：LED Flashing”and double left-click
“Project\_03\_LED\_Flashing.py” to open it. As shown in the
illustration below：

![](/media/e8d875ca48b359b3fe7df7f705dc97e4.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>led = Pin(15, Pin.OUT) # create LED object from Pin 15, Set Pin 15 to output</p>
<p>try:</p>
<p>while True:</p>
<p>led.value(1) # Set led turn on</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>led.value(0) # Set led turn off</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer.
Click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” and see what will
display in the“**Shell**”window.

![](/media/c78c222938d7337d595b3a753fdf702e.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”，the code starts to be
executed and the LED starts flashing. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/d936f3f5a18081cd7539033991daf98b.png)

![](/media/2dcc6a55b77b4175b5175f717eb196c3.png)

**Note**: This is the code running online. If you disconnect the USB
cable and repower ESP32 or press its reset button, the LED in the
circuit stops flashing and the following messages will be displayed in
the "Shell" window of Thonny:

![](/media/c2685b285afdb8a2f9e56ac70c874e98.png)

Code running offline（Upload the code to ESP32）：

Make sure the ESP32 has been connected to the computer,
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](/media/df3715e5657c7edecff914d97f43b8de.png)

As shown below, right-click the
file“Project\_03\_LED\_Flashing.py”，select “**Upload to /**”to
upload the code to ESP32.

![](/media/010dbbff20232229cc92d885fda36d7d.png)

Upload“boot.py”in the same way.

![](/media/8cfeb1a3a4fba034c1d67ef272cb1118.png)

Press the reset button of ESP32 and you can see that the LED will flash
in an endless loop.

![](/media/2dcc6a55b77b4175b5175f717eb196c3.png)

**Note**：Code here is running offline. If you want to stop running
offline and enter“**Shell**”, just click
![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”in Thonny.

![](/media/0fc03f7cc11e6d76447e1e670a1d77e8.png)

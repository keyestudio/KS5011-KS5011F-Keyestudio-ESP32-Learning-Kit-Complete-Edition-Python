**Project 21：Relay**

1.  ### **Introduction**
    
    In our daily life, we usually use communication to drive electrical
    equipment, and sometimes we use switches to control electrical
    equipment. If the switch is connected directly to the ac circuit,
    leakage occurs and people are in danger. Therefore, from the
    perspective of safety, we specially designed this relay module with
    NO(normally open) end and NC(normally closed) end.
    
    In this project, we will learn a relatively special and easy-to-use
    switch, which is the relay module.

2.  ### **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7a4832b8ab8659c061b37c4614793e3e.jpeg" style="width:1.17014in;height:0.57153in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.55417in;height:1.35972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/1ea87894c6aa8d475203e447ad5e930a.png" style="width:1.38056in;height:0.73958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/6ba5c3147b32861b2dbc6b9986382c1b.png" style="width:0.88681in;height:1.04722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.11528in;height:0.59722in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Relay Module*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  ### **Component Knowledge**
    
    **Relay:** It is an "automatic switch" that uses a small current to
    control the operation of a large current.
    
    Input voltage：3.3V-5V
    
    Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)

The rated load means that devices with dc voltage of 24V or AC voltage
of 250V can be controlled using 3.3V-5V microcontrollers.

**Schematic diagram of Relay**

![](/media/be1c90d2b52fc2489590e3f702a087bf.emf)

### **Wiring Diagram**

![](/media/1741d3cb0405c740378ef7ef96df6072.png)

### **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
21：Relay”，and then double left-click“Project\_21\_Relay.py”.

![](/media/26d0543fe77e91b7f5d99c31b67963e2.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p># create relay from Pin 15, Set Pin 15 to output</p>
<p>relay = Pin(15, Pin.OUT)</p>
<p># The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.</p>
<p>def relay_on():</p>
<p>relay(1)</p>
<p># The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.</p>
<p>def relay_off():</p>
<p>relay(0)</p>
<p># Loop, the relay is on for one second and off for one second</p>
<p>while True:</p>
<p>relay_on()</p>
<p>time.sleep(1)</p>
<p>relay_off()</p>
<p>time.sleep(1)</p></td>
</tr>
</tbody>
</table>

### **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/2929f4abc3196645c4d5d2ed54542630.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the relay will cycle on and off, on for 1
second, off for 1 second.  At the same time, you can hear the sound of
the relay on and off, and you can also see the change of the indicator
light on the relay. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/4a5a3673874d5e5a942645b12c652621.png)

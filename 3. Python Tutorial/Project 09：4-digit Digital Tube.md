**Project 09：4-digit Digital Tube**

1.  **Introduction**

The 4-digit 7-segment display is a very practical display device and it
is used for devices such as electronic clocks, score counters and the
number of people in the park. Because of the low price, easy to use,
more and more projects will use the 4 Digit 7-segment display. In this
project, we use ESP32 to control the 4-digit 7-segment display to
display digits.

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
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/ee7a4ecd35ef268149e31fb9d62c8227.png" style="width:0.94792in;height:0.71736in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.90694in;height:0.90069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>4-digit 7-segment display Module*1</td>
<td>220Ω Resistor*8</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/ce987bf9a2ab398945c98b34d3f8a003.png)

**4-digit 7-segment display：**It is a device with common cathode and
anode, its display principle is similar to the 1-Digit digital tube
display. Both of them have eight GPIO ports to control the digital tube
display, that is 8 leds. However, here is 4-digit, so it needs four GPIO
ports to control the bit selection end. Our 4 - digit digital tube is
common cathode. 

The following figure shows the pin diagram of the 4-digit digital tube.
G1, G2, G3 and G4 are the control pins. 

![](/media/37113fa53213973132086c285d67686b.png)

[**Schematic
Diagram**](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/9.0.1.1/resultui/html/index.html#/javascript:;)

![](/media/ea75d1b7414bf6f8c187fb32fea9bc83.png)

4.  **Wiring Diagram**

![](/media/313c429f670cd000b61cd3aeee0fef92.png)

5.  **Test Code**
    
    Codes used in this tutorial are saved in“4. Python Tutorial\\2.
    Python Projects”. You can move the codes to any location. For
    example, we save the codes in Disk(D) with the path of “D:\\2.
    Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
09：4-Digit Digital Tube”, then double left-click
“Project\_09\_Four\_Digit\_Digital\_Tube.py”.

![](/media/cc79af4fa543bfe30f5d07a191543987.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Pin of each digit of nixie tube</p>
<p>a = Pin(18, Pin.OUT)</p>
<p>b = Pin(13, Pin.OUT)</p>
<p>c = Pin(2, Pin.OUT)</p>
<p>d = Pin(16, Pin.OUT)</p>
<p>e = Pin(17, Pin.OUT)</p>
<p>f = Pin(19, Pin.OUT)</p>
<p>g = Pin(0, Pin.OUT)</p>
<p>dp = Pin(4, Pin.OUT)</p>
<p>G1 = Pin(21, Pin.OUT)</p>
<p>G2 = Pin(22, Pin.OUT)</p>
<p>G3 = Pin(14, Pin.OUT)</p>
<p>G4 = Pin(15, Pin.OUT)</p>
<p>#digital tube a to dp corresponding development board pins</p>
<p>d_Pins=[Pin(i,Pin.OUT) for i in [18,13,2,16,17,19,0,4]]</p>
<p>#Pin corresponding to digital tube segment G1, G2, G3, and G4</p>
<p>w_Pins=[Pin(i,Pin.OUT) for i in [21,22,14,15]]</p>
<p>number=</p>
<p>def display(num,dp):</p>
<p>global number</p>
<p>count=0</p>
<p>for pin in d_Pins:#displays the value of num</p>
<p>pin.value(number[num][count])</p>
<p>count+=1</p>
<p>if dp==1:</p>
<p>d_Pins[7].value(0)</p>
<p>def clear():</p>
<p>for i in w_Pins:</p>
<p>i.value(0)</p>
<p>for i in d_Pins:</p>
<p>i.value(1)</p>
<p>def showData(num):</p>
<p>#the hundreds, thousands, ones, and fractional values of a numeric value</p>
<p>d_num=num</p>
<p>location=d_num.find('.')</p>
<p>if location&gt;0:</p>
<p>d_num=d_num.replace('.','')</p>
<p>while len(d_num)&lt;4:</p>
<p>d_num='0'+d_num</p>
<p>for i in range(0,4):</p>
<p>time.sleep(2)</p>
<p>clear()</p>
<p>w_Pins[3-i].value(1)</p>
<p>if i==location-1:</p>
<p>display(d_num[i],1)</p>
<p>else:</p>
<p>display(d_num[i],0)</p>
<p>if location&lt;0:</p>
<p>for i in range(0,4):</p>
<p>time.sleep(2)</p>
<p>clear()</p>
<p>w_Pins[3-i].value(1)</p>
<p>display(d_num[i],0)</p>
<p>while True:</p>
<p>num='9016'</p>
<p>showData(num)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/85eea60de94eac91a459816cc526bffd.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that 4-digit 7-segment display displays
digits，and repeat these actions in an infinite loop. Press “Ctrl+C” or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” to exit the program.

![](/media/317745a0483e0aa755118f2163375e9e.png)

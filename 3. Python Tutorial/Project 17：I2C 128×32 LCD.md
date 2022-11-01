**Project 17： I2C 128×32 LCD**

1.  **Introduction**
    
    In everyday life, we can do a host of experiments with the display
    module and also DIY a broad menu of small objects. For example, you
    can make a temperature meter with a temperature sensor and a
    display, or make a distance meter with an ultrasonic module and a
    display. 
    
    In this project, we will use the LCD\_128X32\_DOT module as the
    display and connect it to the ESP32, which will be used to control
    the LCD\_128X32\_DOT display to show various English words, common
    symbols and numbers.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:2.17847in;height:1.0625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.94722in;height:2.32014in" /></td>
<td></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/2c2645e94a00867ac23e8a022f0a631a.png" style="width:1.59236in;height:0.76736in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/ece3c38dc9a9e6428b122481d6bb0d4d.png" style="width:1.19028in;height:1.00556in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>LCD_128X32_DOT*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

**3.Component Knowledge**

![](/media/2c2645e94a00867ac23e8a022f0a631a.png)

**LCD\_128X32\_DOT**: It is an LCD module with 128\*32 pixels and its
driver chip is ST7567A. The module uses the IIC communication mode,
while the code contains a library of all alphabets and common symbols
that can be called directly.

When using, we can also set it in the code so that the English letters
and symbols show different text sizes. To make it easy to set up the
pattern display, we also provide a mold capture software that converts a
specific pattern into control code and then copies it directly into the
test code for use.

**Schematic diagram of LCD\_128X32\_DOT**

![](/media/5451aed32bc5b7b30fbd5613ad09a65b.png)

**Features:**

Pixel: 128\*32 character

Operating voltage(chip)：4.5V to 5.5V

Operating current：100mA (5.0V)

Optimal operating voltage(module):5.0V

**4. Wiring Diagram**

![](/media/072d954dac310add077688398ad59af2.png)

5.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the codes to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project 17：
I2C 128×32 LCD”. Select“lcd128\_32.py”and
“lcd128\_32\_fonts.py”，right-click your mouse to select“Upload to
/”，wait for“lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to
ESP32，and then double left-click“Project\_17\_I2C\_128\_32\_LCD.py”.

![](/media/9324aa3246b032463d5462c0eb7ac848.png)

![](/media/dfc274fafadf864413e7d1b7f8c91dc4.png)

![](/media/e5135a82011f1291505aff96fc88b7ac.png)

<table>
<tbody>
<tr class="odd">
<td><p>import machine</p>
<p>import time</p>
<p>import lcd128_32_fonts</p>
<p>from lcd128_32 import lcd128_32</p>
<p>#i2c config</p>
<p>clock_pin = 22</p>
<p>data_pin = 21</p>
<p>bus = 0</p>
<p>i2c_addr = 0x3f</p>
<p>use_i2c = True</p>
<p>def scan_for_devices():</p>
<p>    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))</p>
<p>    devices = i2c.scan()</p>
<p>    if devices:</p>
<p>        for d in devices:</p>
<p>            print(hex(d))</p>
<p>    else:</p>
<p>        print('no i2c devices')</p>
<p>if use_i2c:</p>
<p>    scan_for_devices()</p>
<p>    lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)</p>
<p>lcd.Clear()</p>
<p>lcd.Cursor(0, 4)</p>
<p>lcd.Display("KEYESTUDIO")</p>
<p>lcd.Cursor(1, 0)</p>
<p>lcd.Display("ABCDEFGHIJKLMNOPQR")</p>
<p>lcd.Cursor(2, 0)</p>
<p>lcd.Display("123456789+-*/&lt;&gt;=$@")</p>
<p>lcd.Cursor(3, 0)</p>
<p>lcd.Display("%^&amp;(){}:;'|?,.~\\[]")</p>
<p>"""</p>
<p>while True:</p>
<p>    scan_for_devices()</p>
<p>    time.sleep(0.5)</p>
<p>"""</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/a1273c3f5019666f8f2de2b18504e77c.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the 128X32LCD module display will
show“KEYESTUDIO”at the first line，“ABCDEFGHIJKLMNOPQR”will be
displayed at the second line，“123456789+-\*/\<\>=$@”will be shown at the
third line and“%^&(){}:;'|?,.\~\\\\\[\]”will be displayed at the fourth
line. Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart
backend”to exit the program.

![](/media/4834a36715ea72a01498a6077402a033.png)

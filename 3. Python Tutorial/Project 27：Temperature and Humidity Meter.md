# Project 27：Temperature and Humidity Meter 

1.  **Introduction**

In winter, the air is very dry, coupled with cold, the skin of the human
body will be easy to be cracked, so you need to use a humidifier to
increase the humidity of the air at home. However, how to identify
whether the air is too dry? Then you need an equipment to detect the air
humidity.

In this project, we will learn how to use the temperature and humidity
sensor. We will use the sensor to make a
[hygrothermograph](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/9.0.1.1/resultui/html/index.html#/javascript:;),
and combine it with a LCD 128X32 DOT to display the temperature and
humidity values.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:1.59722in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.70139in;height:1.71944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/34bafe8113e2db36c8f0c8492b835474.png" style="width:1.27292in;height:0.96111in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Temperature and Humidity Sensor*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/9232141f8a3166a8a6cdd43b78edd4e3.png" style="width:1.29722in;height:0.625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/f1aed48e2c02214415853ad2358f3744.png" style="width:0.97569in;height:0.82431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.275in;height:0.68264in" /></td>
</tr>
<tr class="even">
<td>LCD 128X32 DOT*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/34bafe8113e2db36c8f0c8492b835474.png)

**Temperature and humidity sensor:** It is a temperature and humidity
composite sensor with calibrated digital signal output, its precision
humidity is±5%RH, temperature is±2℃, and range humidity is 20 to 90%RH,
and temperature is 0 to 50℃.

The temperature and humidity sensor applies to dedicated digital module
acquisition technology and temperature and humidity sensing technology
to ensure extremely high reliability and excellent long-term stability
of the product.

The sensor includes a resistive-type humidity measurement and an NTC
temperature measurement component, which is very suitable for
temperature and humidity measurement applications where accuracy and
real-time performance are not required.

The operating voltage is in the range of 3.3V to 5.5V.

The sensor has three pins, which are VCC、GND and S. S is the pin for
data output, which uses serial communication.

**Definition of Temperature and Humidity Sensor**

<table>
<tbody>
<tr class="odd">
<td><strong>Description</strong></td>
<td><strong>Definition</strong></td>
</tr>
<tr class="even">
<td>Start signal</td>
<td>Microprocessor pulls data bus (SDA) down at least 18ms for a period of time(Maximum is 30ms).</td>
</tr>
<tr class="odd">
<td>Response signal</td>
<td>The sensor pulls the data bus (SDA) low for 83µs, and then pulls up for 87µs to respond to the host's start signal.</td>
</tr>
<tr class="even">
<td>Humidity</td>
<td>The high humidity is an integer part of the humidity data, and the low humidity is a fractional part of the humidity data.</td>
</tr>
<tr class="odd">
<td>Temperature</td>
<td>The high temperature is the integer part of the temperature data, the low temperature is the fractional part of the temperature data. And the low temperature Bit8 is 1, indicating a negative temperature, otherwise, it is a positive temperature.</td>
</tr>
<tr class="even">
<td>Parity bit</td>
<td>Parity bit=humidity high bit+ humidity low bit+temperature high bit+temperature low bit</td>
</tr>
</tbody>
</table>

**Data Sequence Diagram**

When MCU sends a start signal, the temperature and humidity sensor
changes from the low-power-consumption mode to the high-speed mode.
After the start signal ends, the sensor sends a response signal of
40-bit data and triggers a signal acquisition, as shown below:

![](/media/933ac5e5a5e921d4b16c7c48091ba75a.png)

Combined with the code, you can understand better.

The temperature and humidity sensor can easily add temperature and
humidity data to your DIY electronic projects. It is perfect for remote
weather stations, home environmental control systems, and farms or
garden monitoring systems.

**Specification:**

Working voltage: +5V

Temperature range: 0°C to 50°C, error of ± 2°C

Humidity range: 20% to 90% RH,± 5% RH error

Digital interface

**Schematic Diagram**

![](/media/53fa034cbbcec22579b2bdf8252c90cd.emf)

4.  **Read the temperature and humidity values**

![](/media/5d6dd3f19b4323d212bb95e3e4d43743.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
27：Temperature Humidity Meter”and then double left-click
“Project\_27.1\_Detect\_Temperature\_Humidity.py”.

![](/media/3bdfaa1fe69c548bbf255d3e4cbcf2d5.png)

<table>
<tbody>
<tr class="odd">
<td><p># Import machine, time and dht modules.</p>
<p>import machine</p>
<p>import time</p>
<p>import dht</p>
<p>#Associate DHT11 with Pin(13).</p>
<p>DHT = dht.DHT11(machine.Pin(13))</p>
<p># Obtain temperature and humidity data once per second and print them out.</p>
<p>while True:</p>
<p>DHT.measure() # Start DHT11 to measure data once.</p>
<p># Call the built-in function of DHT to obtain temperature</p>
<p># and humidity data and print them in “Shell”.</p>
<p>print('temperature:',DHT.temperature(),'℃','humidity:',DHT.humidity(),'%')</p>
<p>time.sleep_ms(1000)</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/671d402c384352f34d8e5938d4b6a247.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the "Shell" window of Thonny IDE will print
the current temperature and humidity value, as shown below.
Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to
exit the program.

![](/media/0f06c1e7a47dc8ad49e9accccc69924b.png)

![](/media/b5bec7ab305a8ce2e8f702a6040faf83.png)

![](/media/3561864f71474f8e8c7206c07c8d054e.png)

5.  **Wiring Diagram**

Now we start to print the values of the temperature and humidity sensor
with LCD\_128X32\_DOT, then we will see the corresponding values on it.
Please connect wires according to the following wiring diagram：

![](/media/6c82bb28bd1fcd7a1f72108e8a4a70b6.png)

6.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
27：Temperature Humidity Meter”.
Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”，then select“Upload
to /”，and wait for the “lcd128\_32.py”and “lcd128\_32\_fonts.py”to be
uploaded to ESP32，then double
left-click“Project\_27.2\_Temperature\_Humidity\_Meter.py”.

![](/media/ed7c7539ae33fd01619dee51db1a1c63.png)

![](/media/f1989b1172228e125a3c1ad7173497ae.png)

![](/media/e1689125435e50dd30abb9601941fe67.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import machine</p>
<p>import dht</p>
<p>import time</p>
<p>import lcd128_32_fonts</p>
<p>from lcd128_32 import lcd128_32</p>
<p>temp = 0</p>
<p>humi = 0</p>
<p>#Associate DHT11 with Pin(13).</p>
<p>DHT = dht.DHT11(Pin(13))</p>
<p>#i2c config</p>
<p>clock_pin = 22</p>
<p>data_pin = 21</p>
<p>bus = 0</p>
<p>i2c_addr = 0x3f</p>
<p>use_i2c = True</p>
<p>def scan_for_devices():</p>
<p>i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))</p>
<p>devices = i2c.scan()</p>
<p>if devices:</p>
<p>for d in devices:</p>
<p>print(hex(d))</p>
<p>else:</p>
<p>print('no i2c devices')</p>
<p>try:</p>
<p>while True:</p>
<p>DHT.measure()</p>
<p>temp = int(DHT.temperature())</p>
<p>humi = int(DHT.humidity())</p>
<p>if use_i2c:</p>
<p>scan_for_devices()</p>
<p>lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)</p>
<p>lcd.Clear()</p>
<p>lcd.Cursor(0, 0)</p>
<p>lcd.Display("temper:")</p>
<p>lcd.Cursor(0, 8)</p>
<p>lcd.Display(str(temp))</p>
<p>lcd.Cursor(0, 11)</p>
<p>lcd.Display("C")</p>
<p>lcd.Cursor(2, 0)</p>
<p>lcd.Display("Humid:")</p>
<p>lcd.Cursor(2, 7)</p>
<p>lcd.Display(str(humi))</p>
<p>lcd.Cursor(2, 10)</p>
<p>lcd.Display("%")</p>
<p>time.sleep(0.1)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

**7.Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend” .

![](/media/d5efc6dc924fb24859680b3355e7455c.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that the LCD 128X32 DOT will display the current
temperature and humidity value. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/d3d0e7b4ed772ed627dcb1b58cf89238.png)

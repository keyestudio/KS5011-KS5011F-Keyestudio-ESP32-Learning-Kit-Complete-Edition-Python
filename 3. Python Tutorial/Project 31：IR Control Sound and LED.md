**Project 31：IR Control Sound and LED**

1.  **Introduction**

IR remote control is a low-cost and easy-to-use wireless communication
technology. IR light is very similar to visible light, except that its
wavelength is slightly longer. This means that infrared rays cannot be
detected by the human eyes, which is perfect for wireless communication.

For example, when you press a button on the TV remote control, an
infrared LED will be on and off repeatedly at a frequency of 38,000
times per second, transmitting information (such as volume or channel
control) to the infrared sensor on the TV.

We'll start by explaining how common infrared communication protocols
work. Then we will start the project with a remote control and an
infrared receiver component.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/146cead9d42f214abdbcd383a95eb998.jpeg" style="width:1.41458in;height:0.69097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.55278in;height:1.35486in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/88e6b057fb4b0c576c9b2111d15b26e5.png" style="width:1.14861in;height:0.48403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/f1a86fc81ab4b043263ce7e01e14d470.png" style="width:0.23056in;height:1.27847in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>IR Receiver *1</td>
<td>RGB LED*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/8a6fb37dedef748e6c2609bff5c64906.png" style="width:0.69792in;height:1.45764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:0.86111in;height:0.70069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/a22dac8c5edbe90e867cbb04769d1816.png" style="width:0.23194in;height:1.04028in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
</tr>
<tr class="even">
<td>IR Remote Control*1</td>
<td>Active Buzzer*1</td>
<td>10KΩResistor*1</td>
<td>220ΩResistor*3</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/9197d4aff9356c585b7ef68e33a6881d.png" style="width:0.27986in;height:1.08819in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.90694in;height:0.90139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>NPN Transistor(S8050)*1</td>
<td>1kΩResistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**IR Remote Control** ：It is a device with a certain number of buttons.
Pressing different buttons will cause the IR transmitter tubes in the
front of the remote control to send IR signals in different codes.

IR remote control technology is widely used in electronic products such
as TVs and air
[conditioner](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/9.0.1.1/resultui/html/index.html#/javascript:;)s,
etc, making it more accessible for you to switch TV programs and adjust
the temperature of the air
[conditioner](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/9.0.1.1/resultui/html/index.html#/javascript:;)s.
The remote control we use is shown below:

The IR remote control adopts NEC code and the signal cycle is 110ms.

![](/media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

**IR Receiver：**It is a component that can receive IR light, so we can
use it to detect the signals emitted by the IR remote control.

The IR receiver demodules the received IR signals and converts them back
to binary, then passes the information to the microcontroller.

**IR signal modulation process diagram**

![](/media/3da1969e509f53706643c77d0534eb73.png)

**NEC Infrared communication protocol：**

**NEC Protocol**

To my knowledge the protocol I describe here was developed by NEC (Now
Renesas). I've seen very similar protocol descriptions on the internet,
and there the protocol is called Japanese Format.

I do admit that I don't know exactly who developed it. What I do know is
that it was used in my late VCR produced by Sanyo and was marketed under
the name of Fisher. NEC manufactured the remote control IC.

This description was taken from my VCR's service manual. Those were the
days, when service manuals were filled with useful information\!

**Features**

  - > 8 bit address and 8 bit command length.

  - > Extended mode available, doubling the address size.

  - > Address and command are transmitted twice for reliability.

  - > Pulse distance modulation.

  - > Carrier frequency of 38kHz.

  - > Bit time of 1.125ms or 2.25ms.

**Modulation**

![](/media/da33571c6f0afb94b1ec1d91caba3edb.png)

The NEC protocol uses pulse distance encoding of the bits. Each pulse is
a 560µs long 38kHz carrier burst (about 21 cycles). A logical "1" takes
2.25ms to transmit, while a logical "0" is only half of that, being
1.125ms. The recommended carrier duty-cycle is 1/4 or 1/3

**Protocol**

![](/media/f970404e7bbfb5711fea5c776f689f3a.png)

The picture above shows a typical pulse train of the NEC protocol. With
this protocol the LSB is transmitted first. In this case Address $59 and
Command $16 is transmitted. A message is started by a 9ms AGC burst,
which was used to set the gain of the earlier IR receivers. This AGC
burst is then followed by a 4.5ms space, which is then followed by the
Address and Command. Address and Command are transmitted twice. The
second time all bits are inverted and can be used for verification of
the received message. The total transmission time is constant because
every bit is repeated with its inverted length. If you're not interested
in this reliability you can ignore the inverted values, or you can
expand the Address and Command to 16 bits each\!

Keep in mind that one extra 560µs burst has to follow at the end of the
message in order to be able to determine the value of the last bit.

![](/media/63364daf21e5522c64eb8dfa82f2cef2.png)

A command is transmitted only once, even when the key on the remote
control remains pressed. Every 110ms a repeat code is transmitted for as
long as the key remains down. This repeat code is simply a 9ms AGC pulse
followed by a 2.25ms space and a 560µs burst.

![](/media/afea92a3b5cc1aa2457d2b118b157c84.png)

**Extended NEC protocol**

The NEC protocol is so widely used that soon all possible addresses were
used up. By sacrificing the address redundancy the address range was
extended from 256 possible values to approximately 65000 different
values. This way the address range was extended from 8 bits to 16 bits
without changing any other property of the protocol.

By extending the address range this way the total message time is no
longer constant. It now depends on the total number of 1's and 0's in
the message. If you want to keep the total message time constant you'll
have to make sure the number 1's in the address field is 8 (it
automatically means that the number of 0's is also 8). This will reduce
the maximum number of different addresses to just about 13000.

The command redundancy is still preserved. Therefore each address can
still handle 256 different commands.

![](/media/2f78d1ce7f001926f6b90ad966796e91.png)

Keep in mind that 256 address values of the extended protocol are
invalid because they are in fact normal NEC protocol addresses. Whenever
the low byte is the exact inverse of the high byte it is not a valid
extended address.

4.  **Decoded IR signals**

We connect the IR receiver element to the ESP32 according to the wiring
diagram below:

![](/media/700496cb1e0d5d23fd63c28469dd3fd0.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
31：IR Control Sound and LED”. Select“irrecvdata.py”，right-click your
mouse to select“Upload to /”, and wait for the“irrecvdata.py”to be
uploaded to ESP32，and double left-click
“Project\_31.1\_Decoded\_IR\_Signal.py”

![](/media/ecb357d8c06f7b14095354797f16594b.png)

![](/media/ad8bf51daf991b782a8c4f5e0c746c77.png)

<table>
<tbody>
<tr class="odd">
<td><p># Import the infrared decoder.</p>
<p>from irrecvdata import irGetCMD</p>
<p># Associate the infrared decoder with GP0.</p>
<p>recvPin = irGetCMD(0)</p>
<p>#When infrared key value is obtained, print it out in"Shell".</p>
<p>try:</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.</p>
<p>if irValue:</p>
<p>print(irValue)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](/media/e32ae34c4752e612387c7499596ee2e5.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that aim the IR remote control transmitter at
the IR receiver head, press the button on the IR remote control, and
the”Shell” prints the current received key code values.
Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to
exit the program.

![](/media/123ffe7c4396f961678ac94802198f98.png)

![](/media/623f8fa842b90a093d286954835483c6.png)

Write down the code associated with each button, because you will need
that information later.

![](/media/ebcf0cb2055f7784505f76ceeaef9f47.jpeg)

**5. Wiring diagram of the IR remote control**

![](/media/4912c1622e0eaedb76ea3a9b8ed969c0.png)

**6. Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
31：IR Control Sound and LED”. Select“irrecvdata.py”，right-click your
mouse to select“Upload to /”, and wait for the“irrecvdata.py”to be
uploaded to ESP32，and double left-click
“Project\_31.2\_IR\_Control\_Sound\_And\_LED.py”

![](/media/ecb357d8c06f7b14095354797f16594b.png)

![](/media/c571e6d5b41893c77c492da6e9746bfd.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,PWM</p>
<p>import time</p>
<p>from irrecvdata import irGetCMD</p>
<p>#Set RGB light interface and frequency</p>
<p>rgb_r = PWM(Pin(22))</p>
<p>rgb_g = PWM(Pin(21))</p>
<p>rgb_b = PWM(Pin(4))</p>
<p>rgb_r.freq(1000)</p>
<p>rgb_g.freq(1000)</p>
<p>rgb_b.freq(1000)</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(0)</p>
<p>rgb_b.duty(0)</p>
<p># Initialize the buzzer pin</p>
<p>buzzer=Pin(15, Pin.OUT)</p>
<p>#Configure infrared receiving pin and library</p>
<p>recvPin = irGetCMD(0)</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() # Read remote control data</p>
<p># Determine whether there is a button that meets the needs</p>
<p>if irValue:</p>
<p>print(irValue)</p>
<p>buzzer.value(1)</p>
<p>time.sleep(0.1)</p>
<p>buzzer.value(0)</p>
<p>if irValue == '0xff6897': #1</p>
<p>rgb_r.duty(1023)</p>
<p>rgb_g.duty(0)</p>
<p>rgb_b.duty(0)</p>
<p>print('1')</p>
<p>elif irValue == '0xff9867': #2</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(1023)</p>
<p>rgb_b.duty(0)</p>
<p>print('2')</p>
<p>elif irValue == '0xffb04f': #3</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(0)</p>
<p>rgb_b.duty(1023)</p>
<p>print('3')</p>
<p>elif irValue == '0xff30cf': #4</p>
<p>rgb_r.duty(1023)</p>
<p>rgb_g.duty(1023)</p>
<p>rgb_b.duty(0)</p>
<p>print('4')</p>
<p>elif irValue == '0xff18e7': #5</p>
<p>rgb_r.duty(1023)</p>
<p>rgb_g.duty(0)</p>
<p>rgb_b.duty(1023)</p>
<p>print('5')</p>
<p>elif irValue == '0xff7a85': #6</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(1023)</p>
<p>rgb_b.duty(1023)</p>
<p>print('6')</p>
<p>elif irValue == '0xff10ef': #7</p>
<p>rgb_r.duty(1023)</p>
<p>rgb_g.duty(1023)</p>
<p>rgb_b.duty(1023)</p>
<p>print('7')</p>
<p>else:</p>
<p>rgb_r.duty(0)</p>
<p>rgb_g.duty(0)</p>
<p>rgb_b.duty(0)</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](/media/879e29806d6c19b302a5bbc70876ad43.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that press the 1 to 7 keys of the IR remote
control, the buzzer will sound once, and the RGB will be red, green,
blue, yellow,
[carmine](C:/Users/NINGMEI/AppData/Local/youdao/dict/Application/9.0.1.1/resultui/html/index.html#/javascript:;),
blue and green and white respectively. Press another key (except 1 to 7
key), and the RGB will be off. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/707ff7fc1077b22a15defd55ae24beab.png)

**Note**：When the code is running, the following prompt appears, you
just need to click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”，then
click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script” to make the code run
again.

![](/media/3f425db5cda9eb56bc1f29c27fa6696d.png)

(**Note:** Before use, we need to remove the plastic sheet from the
bottom of the IR remote control.)

![](/media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

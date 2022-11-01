**Project 30：Keypad Door**

1.  **Introduction**
    
    Commonly used digital button sensor, a button uses an IO port.
    However, it will occupy many IO ports when we need a lot of buttons.
    In order to save the IO ports, multiple buttons are made into a
    matrix type. In this project, we will use a ESP32 and a 4\*4 matrix
    keyboard to control a servo and a buzzer.

2.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/56053f7126905c6def63919c661d5c0a.jpeg" style="width:1.59722in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.68056in;height:1.66944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/cd0bc424e9916881a1a903793821a042.png" style="width:1.25417in;height:1.04792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:0.86111in;height:0.70069in" /></td>
</tr>
<tr class="even">
<td>ESP32*1</td>
<td>Breadboard*1</td>
<td>Servo*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/fcd187eb009098d691927511606c991b.jpeg" style="width:1.70972in;height:0.74931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.90694in;height:0.90139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
</tr>
<tr class="even">
<td>4*4 Membrane Matrix Keyboard*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td>1kΩResistor*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS5011-KS5011F-Keyestudio-ESP32-Learning-Kit-Complete-Edition-Python/master/media/9197d4aff9356c585b7ef68e33a6881d.png" style="width:0.27986in;height:1.08819in" /></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPN Transistor(S8050)*1</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**4\*4 Matrix keyboard：**It is a device that integrates a number of keys
in a package. As shown below, a 4x4 keypad matrix integrates 16 keys:

![](/media/fcd187eb009098d691927511606c991b.jpeg)

Similar to the integration of an LED matrix, the 4x4 keypad matrix’s
each row of keys is connected with a pin and it is the same in columns,
which can reduce the required numbers of processor ports. The internal
circuit of the keypad matrix is shown below.

![](/media/5ebdacba906622079e0ef41dc1ea3fdf.png)

The method of usage is similar to the LED matrix , we can scan rows and
columns to detect the state of each key. We take the column scanning
method as an example, we need to send low level to the fourth column
(Pin4), and detect the level state of row 1, 2, 3, 4 to judge whether
the key A, B, C, D are pressed. Then we can send low level to column 3,
2, 1 in turn to detect whether other keys are pressed. By this means,
you can get the state of all keys.

4.  **Read the key values of the 4\*4 matrix keyboard：**
    
    We start with a simple code to read the values of the 4\*4 matrix
    keyboard and print them in the serial monitor. Its wiring diagram is
    shown below：

![](/media/8bfa0e1b1a0f53598f51341d51bc7601.png)

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project 30：
Keypad Door”. Select“keypad.py”and “myservo.py”，right-click your mouse
to select“Upload to /”，wait for“keypad.py”and“myservo.py”to be uploaded
to ESP32，and double left-click
“Project\_30.1\_4x4\_Matrix\_Keypad\_Display.py”.

![](/media/66dea026563cb96cfb6372bb38c317ae.png)

![](/media/06116aead495864c279aba697bc4db86.png)

<table>
<tbody>
<tr class="odd">
<td><p># Import keypad module.</p>
<p>from keypad import KeyPad</p>
<p>import time</p>
<p># Associate the keypad module to ESP32 pins.</p>
<p>keyPad = KeyPad(22, 21, 19, 18, 17, 16, 4, 0)</p>
<p>#Call function keyPan.scan() to obtain the value of the pressed key. Once it is obtained, print it out.</p>
<p>def key():</p>
<p>keyvalue = keyPad.scan()</p>
<p>if keyvalue != None:</p>
<p>print(keyvalue, end="\t")</p>
<p>time.sleep_ms(300)</p>
<p>return keyvalue</p>
<p>while True:</p>
<p>key()</p></td>
</tr>
</tbody>
</table>

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](/media/ab3337bcb6610f8f0c6273fe7e4c6f6a.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that press the keyboard and the ”Shell” will
print the corresponding key values, as shown below. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/7bf4c71576be9566ecbc604bc60c5cf8.png)

![](/media/2f82f861d68daaaad8085b6a1bcc2e8d.png)

5.  **Wiring Diagram**

In the last experiment, we have known the key values of the 4\*4 matrix
keyboard. Next, we use it as the keyboard to control a servo and a
buzzer.

![](/media/862e840117a46c1174522a734e28e2f0.png)

6.  **Test Code**

The code used in this tutorial is saved in“4. Python Tutorial\\2. Python
Projects”. You can move the code to any location. For example, we save
the codes in Disk(D) with the path of “D:\\2. Python Projects”.

![](/media/906b7d4391131929a6b0726f7f5bab30.png)

Open“Thonny”，click“This computer”→“D:”→“2. Python Projects”→“Project
30：Keypad Door”. Select“keypad.py”and “myservo.py”，right-click your
mouse to select“Upload to /”，wait for“keypad.py”and“myservo.py”to be
uploaded to ESP32，and double left-click
“Project\_30.2\_Keypad\_Door.py”.

![](/media/66dea026563cb96cfb6372bb38c317ae.png)

![](/media/6af240376e4644aa423a7b327198804b.png)

![](/media/67deb025c0bcd47c71fd51578f1bd576.png)

<table>
<tbody>
<tr class="odd">
<td><p>from myservo import myServo #Import myservo module.</p>
<p>from keypad import KeyPad</p>
<p>from machine import Pin</p>
<p>import time</p>
<p>keyPad = KeyPad(22, 21, 19, 18, 17, 16, 4, 0)</p>
<p>servo=myServo(15)</p>
<p>servo.myServoWriteAngle(0)</p>
<p>time.sleep_ms(1000)</p>
<p>activeBuzzer = Pin(2, Pin.OUT)</p>
<p># Define an array and set the password.</p>
<p>passWord = "1234"</p>
<p>keyIn = ""</p>
<p>def key():</p>
<p>keyvalue = keyPad.scan()</p>
<p>if keyvalue != None:</p>
<p>print('Your input:', keyvalue)</p>
<p>time.sleep_ms(200)</p>
<p>return keyvalue</p>
<p>while True:</p>
<p># Each time a key is pressed, the buzzer will short beep once,</p>
<p># and the key value of the key will be stored in the keyIn array.</p>
<p>keydata = key()</p>
<p>if keydata != None:</p>
<p>activeBuzzer.value(1)</p>
<p>time.sleep_ms(100)</p>
<p>activeBuzzer.value(0)</p>
<p>keyIn += keydata</p>
<p># When 4 keys are pressed, it will judge whether the password is correct.</p>
<p># If it is correct, the servo will rotate 90 degrees, and then turn back after 1 second.</p>
<p># If the password is wrong, the buzzer will long beep once and the keyInNum value will be cleared.</p>
<p>if len(keyIn) == 4:</p>
<p>if keyIn == passWord:</p>
<p>print("passWord right!")</p>
<p>servo.myServoWriteAngle(90)</p>
<p>time.sleep_ms(1000)</p>
<p>servo.myServoWriteAngle(0)</p>
<p>else:</p>
<p>print("passWord error!")</p>
<p>activeBuzzer.value(1)</p>
<p>time.sleep_ms(1000)</p>
<p>activeBuzzer.value(0)</p>
<p>keyIn = ""</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**

Make sure the ESP32 has been connected to the computer, then
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](/media/2fe6d56185a05e8278eb4598f07878f2.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts to be
executed and you'll see that press the keypad to input password with 4
characters. If the input is correct(Correct password :1234), the servo
will move to a certain degree, and then return to the original position.
If the input is wrong, an input error alarm will be generated.

Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to
exit the program.

![](/media/5df783f97058fd8a4c4baf5445d3954e.png)

![](/media/d45bd766b2b2630219f8bef283a07417.png)

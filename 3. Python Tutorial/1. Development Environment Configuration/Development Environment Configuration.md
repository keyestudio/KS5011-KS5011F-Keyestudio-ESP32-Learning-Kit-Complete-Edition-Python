# **Development Environment Configuration**

**1. Install Thonny：**

Thonny is a free and open source software platform with small size,
simple interface, simple operation and rich functions. It is a Python
IDE suitable for beginners. In this tutorial, we use this IDE to develop
a ESP32. Thonny supports multiple operating systems including Windows,
Mac OS, Linux.

2.  **Download Thonny：**

<!-- end list -->

1)  Enter the
    website：[<span class="underline">https://thonny.org</span>](https://thonny.org)
    to download the latest version of Thonny.
    
    (2)Thonny open-source code
    library：[<span class="underline">https://github.com/thonny/thonny</span>](https://github.com/thonny/thonny).

<table>
<tbody>
<tr class="odd">
<td>System</td>
<td>Download link</td>
</tr>
<tr class="even">
<td>MAC OS：</td>
<td><a href="https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg">https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg</a></td>
</tr>
<tr class="odd">
<td>Windows：</td>
<td><a href=" https:/github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe">https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe</a></td>
</tr>
<tr class="even">
<td>Linux：</td>
<td><p>Latest version:</p>
<p><strong>Binary bundle for PC (Thonny+Python):</strong></p>
<p>bash &lt;(wget -O - https://thonny.org/installer-for-linux)</p>
<p><strong>With pip:</strong></p>
<p>pip3 install thonny</p>
<p><strong>Distro packages (may not be the latest version):</strong></p>
<p><strong>Debian, Rasbian, Ubuntu, Mint and others:</strong></p>
<p>sudo apt install thonny</p>
<p><strong>Fedora:</strong></p>
<p>sudo dnf install thonny</p></td>
</tr>
</tbody>
</table>

![](/media/bd5823ede2c01d1fa4696438c62aec51.png)

3.  **Windows System**

<!-- end list -->

1.   The downloaded Thonny icon is as follow:
    
    ![](/media/d3caa98d406fa06a124d5c98195b90db.png)

2.  Double-click“thonny-3.3.13.exe”and select install mode. You can
    choose ![](/media/37be3f3bcc9aa0eb48c8b844eb46a71c.png)
    
    ![](/media/4c044b255da8b14fe674eb9cce01627d.png)

3.  You can also keep selecting **Next** to finish the installation.
    
    ![](/media/995b36640124b6a9b23f10473ff8a38a.png)
    
    ![](/media/8bcc17840b9fc15d76f79fee8a0168ee.png)

4.  If you want to change the route of installing Thonny，just
    click“**Browse...**”to select a new route and click **OK**.
    
    ![](/media/df6f63b42ebb1676b22c26b25dc9c7aa.png)
    
    ![](/media/f5cd6d619b4645601c5b098ffdbec12a.png)

5.  Click **Create desktop icon,** you will view Thonny on your desktop.

![](/media/a30c89dde3de81ad00aced30510071be.png)

6.  Click“**Install**”
    
    ![](/media/6ace65142291e5e8af5f81e4a6b2f180.png)

7.  Wait for a while but don’t click **Cancel**
    
    ![](/media/a504b3a3ab16b4d91040cd5878acea0c.png)
    
    G. Click**“Finish”**
    
    ![](/media/a1fb6027e54a975de1c0aa1e1a0d6a29.png)
    
    ![](/media/80f35044d91d66f734e36059db35f273.png)

<!-- end list -->

2.  **Basic Setting：**
    
    Double-click Thonny, choose language and initial settings and click
    **Let’s go！**
    
    ![](/media/ee240978a4f844184f1ea9f5a21d0395.png)
    
    ![](/media/619a856895d95e00beed748b1438072d.png)
    
    ![](/media/bcf6c31e4f69c904a7a0c0e9df7e8d7d.png)

<!-- end list -->

1.  Click“**View**”→“**File**”and“**Shell**”
    
    ![](/media/5ff5c305585dbe7e832cc41183db5818.png)
    
    ![](/media/d41b79772c9846fd8bf295c8451f8321.png)
    
    ![](/media/3d04fe6893ca104e4e593a0786cb3799.png)
    
    **Install the CP2102 driver：**
    
    Before using the Thonny, we need to install the CP2102 driver in the
    computer.

**Windows system**

Check if the CP2102 driver has been installed

1. Interface the ESP32 with your PC with a USB cable

![](/media/c76d1a3ec06e5f3d2cf4a2d9c5b5f4f9.png)

2. Click“This PC”and right-click Manage”

![](/media/84bc1f7d3169cad24b23d2ac620bc111.png)

3.  Click“Device Manager”, if the CP2102 driver has been
    installed，Silicon Labs CP210x USB to UART Bridge(COMx) will be
    shown.
    
    ![](/media/a320816d8aed54304018d8380b5b6b3d.png)
    
    If the CP2102 has not been installed
    
    ![](/media/776adb879fe6e299e3610cc92cfaf70b.png)
    
    Click“CP2102USB to UART Bridge Controller”and Update driver”.
    
    ![](/media/7b342fbd38b03cba4dfce2045f4fe17b.png)
    
    Click“Browse my computer for drivers ”.
    
    ![](/media/1cb9eaea189e4766d17a0a5977c23a74.png)
    
    Click Browse... to choose CP210x\_6.7.4 (“4. Python Tutorial\\1.
    Development Environment Configuration\\CP2102 Driver File-Windows”)
    and click Next
    
    ![](/media/b1995fce2ccc024f32a9b9b83cbc28a6.png)
    
    The CP2102 driver will be installed
    
    ![](/media/b99fbcb61c133392d1b94b65f51fc2c7.png)
    
    ![](/media/da0dffd89b5f385612c3230422ee732f.png)

**MAC System**

You can refer to the file “Development Environment Configuration”，the
route is：“3. Arduino Tutorial\\1. Development Environment
Configuration--Mac”.

![](/media/cb1eb7f4caf6596bd40d20ead2a67368.png)

**3. Burn Micropython firmware**

To run a Python program on the ESP32 board, we need to burn the firmware
to the ESP32 board first.

Download Micropython firmware

microPython website：<http://micropython.org/>

ESP32
firmware：[<span class="underline">https://micropython.org/download/esp32/</span>](https://micropython.org/download/esp32/)

![](/media/c706d3cd6862323dcfccfd11ec7d1da3.png)

The firmware we use：**esp32-20210902-v1.17.bin**

Download
firmware：[https://micropython.org/resources/firmware/esp32-20210902-v1.17.bin](https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin)

Firmware：“4. Python\_Tutorial\\1. Development Environment
Configuration\\Python\_Firmware”.

![](/media/7fb8378937eb6b74989840f982af5fb9.png)

Burn the Micropython firmware

Connect the ESP32 to your PC with a USB cable

![](/media/d59fe9d9aced2ab49f5b9c6e59d9afde.jpeg)

![](/media/c76d1a3ec06e5f3d2cf4a2d9c5b5f4f9.png)

Make sure the driver has been installed successfully and the COM port
can be identified correctly. Open Device Manager and  expand “Ports”.

![](/media/d154c68ab7e252cf013b374069a2c6c0.png)

Open Thonny，click“run”and“Select interpreter...”

![](/media/bda2bfc9d4576aef0b63e1f6373bf5a7.png)

Select Micropython (ESP32) and Silicon Labs CP210x USB to UART
Bridge(COM3) and click “Install or update firmware”.

![](/media/adfa634e977c803db209b18418f1df76.png)

Select“Silicon Labs CP210x USB to UART Bridge(COM3)”，click “
Browse...”and choose the firmware **esp32-20210902-v1.17.bin.**
Check“Erase flash before installing”and“Flash mode”，then
click“Install”.

（(Note：If you fail to install the firmware，press the Boot button on the
ESP32 board and click“Install”）

![](/media/8b746aeb78c731ab638141c8c197437b.png)

![](/media/6e13c0f08fdbf4586295c6c224f38b91.png)

![](/media/055d392fe9a633564b3608128c7fd0a7.png)

Then click Close and OK

![](/media/f706c7f121e659e206fd9727665f1af2.png)

![](/media/5ff623e84c9a432edeb9534fe563f172.png)

![](/media/7fc6ac0c25d55775ef60449f497c6f2f.png)

Turn off all windows and turn to the main page and click
![](/media/a807dd85c760f2bda89025b9fd70156e.png)“STOP.

![](/media/e9d1c2d43c22cf13ada2bdf4808aacb9.png)

**Test Code**

Test the Shell commander

Input print('hello world') in the“Shell”and press **Enter**

![](/media/0dd4176ed13f85a7c96c14b4e20e6166.png)

**Run the test code(online)**

Connect the ESP32 to your PC. Users can program and debug programs with
Thonny.

Open Thonny and click Open.

![](/media/7fded176b193d1ac598571f7d16599f7.png)

When a new window pops up, click“This computer”

![](/media/101bf94e8e29ce5bc4a948f15b5dbe51.png)

Select the file“Project\_01\_HelloWorld.py”

![](/media/06cec75374d1818e56341ef87a090411.png)

Click ![](/media/31511be865975be04b53f27aa45c60a7.png),“Hello World”will be printed in
the“Shell”monitor.

![](/media/95686a34ef893fbad426628f8eedbdc6.png)

Note: Press the reset button to reboot

**Run the test code(offline)**

After rebooting the ESP32, run the boot.py file under the root directory
first then run your code file.

So, we need to add a guide program to run the code of users.

Move the file“4. Python Tutorial\\2. Python Projects” to the disk(D)，the
route is“D:/2. Python Projects”, then open the “Thonny”.

![](/media/000a950d20ba8d5cb478cbeb33dd238c.png)

Click project 00. Boot.Boot and double-click boot.py, then the code
under MicroPython device can run offline.

![](/media/da4d70e3edebeaba6bb5fa6247a777b9.png)

If you want to run the code offline, you nee to upload boot.py and
program code to MicroPython device, then press the ESP32’s reset button.
We will take the project 00 and project 01 as an example. Select boot.py
and right-click Upload to /.

![](/media/4322dafa440f20bea8bca8b5f0437b17.png)

Similarly, upload the project\_01\_Helloworld. py file to the
"MicroPython Device". 

![](/media/5734425738777d7a79a7e0abc4d65106.png)

Press the Reset button, you will view code running in the Shell monitor

![](/media/40e0e288b6b228b8a906054d8b602869.png)

Upload the code to the ESP32

We take the boot.py as an example. If we add a boot.py in each code
directory, reboot the ESP32, the boot.py will run first.

![](/media/2a33e5afa8793c96d69255afb9067f15.png)

Select “boot.py”in the file Project 03：LED Flashing, right-click to
select“Upload to /”. Then the code will be uploaded to the root
directory of the ESP32 and click OK.

![](/media/f3bca24026e4beda4f05ccd89cbeea14.png)

![](/media/14a519166b9f9e7b3420812fb4295210.png)

Download the code to your PC:

MicroPython device\<boot.py, then right-click Download to…

![](/media/cf9de37f4565f94e386542c777403dc3.png)

Delete files of the ESP32

For example, click“boot.py”in the MicroPython device and right-click
Delete.

![](/media/70e75f7f9f40b454dd3a3b580b736b2f.png)

Select boot.py in the Project 03：LED Flashing folder, right-click Move
to Recycle Bin to delete it.

![](/media/646bb65f65361eb2c70b4abf40fc74ea.png)

Create and save code

Click“File”→“New”to create and edit code.

![](/media/1d71df4720f9455dcaf17a72ec38bb1b.png)

Enter the code in the new file. We take the
Project\_03\_LED\_Flashing.py as an example.

![](/media/e80d2f6ce955d013a708fd7134d6e64a.png)

Click ![](/media/40348c4ef49beb5e90593df6050c1d62.png) to save the code to your PC or the ESP32.

![](/media/0f184894cef3d5d00a216dc2161d05d0.png)

Select MicroPython device and enter main.py in the new page and click
OK.

![](/media/895a782664e10406ce2ab9ba18507d19.png)

Then the code will be uploaded to the ESP32.

![](/media/cec982987cf6b8cc24d5830e7777ac63.png)

Disconnect the USB cable and connect it, you can see the effect of the
LED flashing continuously in the circuit on a cycle.  

![](/media/2dcc6a55b77b4175b5175f717eb196c3.png)

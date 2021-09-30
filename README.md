# raspberrypiMusicBox

Project to make raspberry pi 4 like music box can command the playlist from every where.....

-----------------------------------------------

ถ้ามันถามรหัส pi คือ 1

# วิธีลงกล่องต่อจากที่ clone มา

เช็ค Serial number จดบันทึกไว้กับกล่อง

```cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2```

ลง Anydesk 

# Install Anydesk

```sudo apt update```

```sudo apt full-upgrade```

```wget https://download.anydesk.com/rpi/anydesk_6.1.1-1_armhf.deb```

```sudo dpkg -i anydesk_6.1.1-1_armhf.deb```

```sudo apt-get install -f```

เข้าไปที่ anydesk ตั้ง Fix รหัสไว้เป็น wmc12345

จด เลขไอดี anydesk ไว้กับกล่อง

ทำ Fake monitor เพื่อให้กล่องสามารถรีโมทได้โดยไม่ต้องต่อจอ

# Fake monitor for Anydesk
https://askubuntu.com/questions/453109/add-fake-display-when-no-monitor-is-plugged-in

```sudo apt-get install xserver-xorg-video-dummy```

เปิด editor ที่ชื่อ nano 

write it in the /usr/share/X11/xorg.conf.d/xorg.conf

```sudo nano /usr/share/X11/xorg.conf.d/xorg.conf```

copy code ข้างล่างนี้ทั้งหมดมาใส่

```
Section "Device"
    Identifier  "Configured Video Device"
    Driver      "dummy"
EndSection

Section "Monitor"
    Identifier  "Configured Monitor"
    HorizSync 31.5-48.5
    VertRefresh 50-70
EndSection

Section "Screen"
    Identifier  "Default Screen"
    Monitor     "Configured Monitor"
    Device      "Configured Video Device"
    DefaultDepth 24
    SubSection "Display"
    Depth 24
    Modes "1024x800"
    EndSubSection
EndSection
```

กด ctl+o แล้ว enter เพื่อ save 

กด ctl+x แล้ว enter เพื่อ ออก

ถอดจอ ถอดสายไฟ 


# install this pkg

```sudo apt-get install python3-alsaaudio ```

```sudo pip3 install psutil ```

```sudo pip3 install requests ```

```sudo pip3 install tqdm ```

```sudo python3 -m pip install pygame==2.0.1```

```sudo pip3 install speedtest-cli```

```sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 libsdl2-ttf-2.0-0```

```sudo pip3 install pause```

# Set auto run

1.Create service file in /lib/systemd/system/nine.service

```sudo nano /lib/systemd/system/nine.service```

```[Unit]
Description=Dummy Service
After=network-online.target network.target sound.target syslog.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=python3 /home/pi/raspberrypiMusicBox/testThreading.py
WorkingDirectory=/home/pi/raspberrypiMusicBox
Restart=on-failure
StandardOutput=inherit
StandardError=inherit

[Install]
WantedBy=multi-user.target 
```

2.Set up chmod

```sudo chmod 777 /lib/systemd/system/nine.service```

```sudo chmod 777 /home/pi/raspberrypiMusicBox/testThreading.py```

3.Enable service 

```sudo systemctl enable nine.service```

4.Set service run on startup 

```sudo systemctl daemon-reload```


# Service Task
## Check status

```sudo systemctl status nine.service```

## Start 

```sudo systemctl start nine.service```

## Stop

```sudo systemctl stop nine.service```

# Check service's log

```sudo journalctl -f -u nine.service```


# speacial case

Go to root user by this command
```sudo -i```

update pygame 1.9 to 2.0

```python3 -m pip install -U pygame --user```

# Install Anydesk
```sudo apt update```

```sudo apt full-upgrade```

```wget https://download.anydesk.com/rpi/anydesk_6.1.1-1_armhf.deb```

```sudo dpkg -i anydesk_6.1.1-1_armhf.deb```

```sudo apt-get install -f```

# Fake monitor for Anydesk
https://askubuntu.com/questions/453109/add-fake-display-when-no-monitor-is-plugged-in

```sudo apt-get install xserver-xorg-video-dummy```

write it in the /usr/share/X11/xorg.conf.d/xorg.conf

```sudo nano /usr/share/X11/xorg.conf.d/xorg.conf```

```
Section "Device"
    Identifier  "Configured Video Device"
    Driver      "dummy"
EndSection

Section "Monitor"
    Identifier  "Configured Monitor"
    HorizSync 31.5-48.5
    VertRefresh 50-70
EndSection

Section "Screen"
    Identifier  "Default Screen"
    Monitor     "Configured Monitor"
    Device      "Configured Video Device"
    DefaultDepth 24
    SubSection "Display"
    Depth 24
    Modes "1024x800"
    EndSubSection
EndSection
```

# Check Serial

```cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2```

# Set crontab 

`sudo nano launcher.sh`

```
#!/bin/sh
#sudo launcher.sh

cd /
cd home/pi/raspberrypiMusicBox
sudo python3 testThreading.py
```

`sudo chmod 777 launcher.sh`

test run

`sh launcher.sh`

Create logs folder

`mkdir logs`

`sudo crontab -e `

`@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1`

reboot 

# Set crontab for reboot every day

sudo crontab -e

# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
44 14 * * * /sbin/shutdown -r now


# วิธีปิดตัว AUX ไปใช้ตัว USB แทน

1.Disable onboard audio

Open `/etc/modprobe.d/raspi-blacklist.conf and add blacklist snd_bcm2835.`

2.Allow the USB audio device to be the default device.

Open `/lib/modprobe.d/aliases.conf` and comment out the line `options snd-usb-audio index=-2`

3.

`sudo reboot`

# Set buffer

`sudo nano /etc/pulse/daemon.conf`

เลื่อนมาล่างสุดแก้ค่าเป็น 

; default-fragments = 5
; default-fragment-size-msec = 2

# Hot-install

```sudo apt-get install python3-alsaaudio ```

`sudo crontab -e `

# Set auto run

1.Create service file in /lib/systemd/system/nine.service

```sudo nano /lib/systemd/system/nine.service```

```[Unit]
Description=Dummy Service
After=network-online.target network.target sound.target syslog.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=python3 /home/pi/raspberrypiMusicBox/testThreading.py
WorkingDirectory=/home/pi/raspberrypiMusicBox
Restart=on-failure
StandardOutput=inherit
StandardError=inherit

[Install]
WantedBy=multi-user.target 
```

2.Set up chmod

```sudo chmod 777 /lib/systemd/system/nine.service```

```sudo chmod 777 /home/pi/raspberrypiMusicBox/testThreading.py```

3.Enable service 

```sudo systemctl enable nine.service```

4.Set service run on startup 

```sudo systemctl daemon-reload```

# วิธีปิดตัว AUX ไปใช้ตัว USB แทน

1.Disable onboard audio

Open `sudo nano /etc/modprobe.d/raspi-blacklist.conf and add `blacklist snd_bcm2835`.`

2.Allow the USB audio device to be the default device.

Open `sudo nano /lib/modprobe.d/aliases.conf` and comment out the line `options snd-usb-audio index=-2`

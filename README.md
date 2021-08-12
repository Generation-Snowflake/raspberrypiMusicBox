# raspberrypiMusicBox

Project to make raspberry pi 4 like music box can command the playlist from every where.....

# install this pkg

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

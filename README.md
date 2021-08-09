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



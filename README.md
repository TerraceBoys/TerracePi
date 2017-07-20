# TerracePi

## Setting up the Pi

Setting up Wifi (Not needed with new Pis): 
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Install VNC & Start on Boot (Not needed with Noobs 2.4+): 
https://www.raspberrypi.org/documentation/remote-access/vnc/
- Edit rc.local `sudo nano /etc/rc.local`
- Add `sudo /etc/init.d/vncboot start`

Start Script on Boot & Nightly @ 3am:
- `crontab -e`
- Add `0 3 * * * /home/pi/Desktop/TerracePi/refresh.sh &`
- Add `@reboot /home/pi/Desktop/TerracePi/refresh.sh &`

Configuring Environment
- 'sudo apt-get update'
- 'sudo apt-get install python-dev python-imaging'
- 'wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip'
- 'unzip master.zip'
- 'cd rpi-rgb-led-matrix-master/'
- 'make' (rgbmatrix.so)

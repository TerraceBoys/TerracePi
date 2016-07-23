# TerracePi

## Setting up the Pi

Setting up Wifi: 
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Install VNC & Start on Boot: 
https://www.raspberrypi.org/documentation/remote-access/vnc/
- Edit rc.local `sudo nano /etc/rc.local`
- Add `sudo /etc/init.d/vncboot start`

Start Script on Boot & Nightly @ 3am:
- `crontab -e`
- Add `0 3 * * * * /home/pi/Desktop/TerracePi/refresh.sh &`
- Add `@reboot /home/pi/Desktop/TerracePi/refresh.sh &`

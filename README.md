### Backpack with LTE and wi-fi


## The Idea

You have a SIM card with unlimited Internet data bundle. You have another SIM card, that you use
in youre phone. You want to use unlimited Internet and keep your phone number. So you get an LTE
modem, and share the connection via Wi-Fi.


### Hardware

* Raspberry Pi Zero W
* LTE modem _(D-Link DWM-221 in my case)_
* SIM card with Internet
* SD card
* Battery pack _(better 2 for swapping)_
* USB micro-to B cable _(for modem)_
* USB micro-to-A cable _(for battery)_
* Raspberry Pi Zero Case
* Case for Goggles
* Backpack


## Do It

Get Raspberry Pi Zero W, install Raspbian on it, update it.


### Setup LTE modem

Refer to http://wiredtron.com/2018/07/07/raspberry-pi-with-huawei-E397u-53-dongle-metro/.

#### Hints

- I'm using [/etc/qmi-network.conf](etc/qmi-network.conf).

- To reset PIN protection of your SIM card, get inspiration from these commands:

```
  sudo qmicli -d /dev/cdc-wdm0 --dms-uim-get-pin-status
  sudo qmicli -d /dev/cdc-wdm0 --dms-uim-set-pin-protection=PIN,disable,1234
  sudo qmicli -d /dev/cdc-wdm0 --dms-uim-get-pin-status
```


### Setup Access Point

Refer to https://scribles.net/creating-wireless-router-using-raspberry-pi-zero-w/ for the whole process,
use _wwan0_ instead of _wlan1_.


### Extra

Setup basic *status* HTTP server. Check [http-server.py](http-server.py), [stats](stats) for the
sources, and [etc/systemd/system/http-server.service](etc/systemd/system/http-server.service) for
the service definition.

Enabling the service then is done with these commands:

```
sudo systemctl enable http-server
sudo systemctl status http-server
sudo systemctl start http-server
sudo systemctl status http-server
```

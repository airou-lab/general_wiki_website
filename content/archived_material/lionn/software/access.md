# Accessing the Drone

## Connecting to the VOXL

ModalAI provides a [Developer Bootcamp for the VOXL](https://docs.modalai.com/voxl-developer-bootcamp/) which contains lots of useful information and the basic setup steps we used.

Developers may connect to the VOXL in one of the following ways, but [Wireless via DEV Network](#wireless-ssh-via-dev-network) is currently configured.

### Wired via microUSB using ADB

Be sure to connect using the built-in microUSB port, not the USB extension.

0. Assure the VOXL is powered on.
1. Connect the VOXL and developer machine using microUSB-to-USB-A cable.
2. Run `adb`

For more information, see the [VOXL adb setup guide](https://docs.modalai.com/setting-up-adb/).

### Wireless SSH via VOXL Network

The VOXL can be configured to transmit a wireless network.

0. Assure the VOXL is powered on.
1. First, connect to the wireless network (named `voxl-wifi`) using the default password `1234567890`.
2. To SSH into the VOXL, run `ssh root@192.168.8.1`, providing the default password `oelinux123`.

For more information, see the [VOXL wifi setup guide](https://docs.modalai.com/voxl-wifi-setup/).

### Wireless SSH via DEV Network

The VOXL and NUC are can beconfigured to connect to an existing development network.

0. Assure the VOXL, NUC, and development PC are powered on.
1. On the development PC, turn on wifi and the broadcast using the Ubuntu Settings GUI.
2. On the development PC, SSH into the VOXL using the following BASH command. Ensure you are connecting to the root user.
```bash
ssh root@10.42.0.139
```
3. Provide the root password (default `oelinux123`).

For more information, see the [VOXL wifi setup guide](https://docs.modalai.com/voxl-wifi-setup/).

### Web Interface

The VOXL will transmit a web interface summarizing the VOXL's information and giving camera previews.

When on the same network as the VOXL (either its own network or a developer network), this web interface can be found at the VOXL's IP address via http in the web browser (e.g. <http://10.42.0.139/>).

For more information, see the [VOXL Portal guide](https://docs.modalai.com/voxl-portal/)

### QGroundControl

Our development PC is configured to automatically connect to the VOXL whenever the VOXL is connected to its hotspot and QGC is openned.

You can also connect to QGC via the microUSB extension cord (VOXL usb-jst) plugged into the [Flight Core's USB connector](https://docs.modalai.com/voxl-flight-datasheet-connectors/#j1006---usb-connector). This USB connector doesn't connect to the Linux OS on the VOXL, instead connecting directly to the PX4.

For more information, see the [VOXL QGC connection guide](https://docs.modalai.com/qgc-wifi/)
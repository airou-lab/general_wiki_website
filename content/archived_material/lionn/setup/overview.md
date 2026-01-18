# Setup Guide
This document details the steps to implement the setup for the LIONN platform once the hardware is finished and the software is installed.

## Setup VOXL

The [VOXL Developer Bootcamp](https://docs.modalai.com/voxl-developer-bootcamp/) from ModalAI was used to setup the VOXL.

The latest VOXL image was loaded (see [Software](../software/README.md#operating-systems)) and the `voxl-configure-mpa` script to configure the different services on the VOXL based on the hardware shipped with the VOXL Flight Deck (see [voxl-configure-mpa](https://docs.modalai.com/voxl-configure-mpa/))

## Testing VOXL Motor connections

Two methods were used to test if the VOXL was able to control the propeller motors.

***Ensure the propellers are removed before testing!***

### Generate a PWM signal

The main method to test connections is using QGroundControl. Once connected (see [Software Starter Guide < QGroundControl](../software/starter.md#qgroundcontrol)) the QGroundControl app provides configuration for the drone. In the Motor tab, a test slider can be used to power up the motors.

Secondly, when unable to connect the VOXL to QGC, ModalAI provides a [Flight Core PWM ESC Calibration script](https://docs.modalai.com/flight-core-pwm-esc-calibration/) that can be used to bypass QGC.

### Test the PWM signal coming from the VOXL

In order to ensure the PWM connection was provided to the ESCs in the first place, a simple LED circuit was created and connected to the PWM output for one of the 6 motor outputs on the VOXL's PWM breakout board. The LED's ground pin was connected to the PWM ground, and the positive pin was connected to the PWM's power and signal pins.

When the signal was sent using one of the above methods, the LED would flash, indicating the PWM signal being successfully sent.

## Setup NUC

### Network Configuration
[Enable the SSH server on the NUC](https://www.cyberciti.biz/faq/how-to-install-ssh-on-ubuntu-linux-using-apt-get/) and [configure the firewall](https://www.cyberciti.biz/faq/howto-configure-setup-firewall-with-ufw-on-ubuntu-linux/), enabling ssh connections (port 22). Ensure that in the `/etc/ssh/sshd_config` file, `PasswordAuthentication yes` exists as a line.

Enable wifi using `nmcli` and connect to the VOXL's wifi network.
Now, once connected to the VOXL's wifi network, the developer computer can SSH into both the VOXL and the NUC.

The NUC and VOXL have instead been configured to network using a wired ethernet adapter. This is done using the `sudo ip ad add IP_ADDRESS/24 dev eth0` command on each device with it's respective IP (see [this guide](https://askubuntu.com/a/116680)).

## Network Summary

The below table summarizes the IPs that each component of the platform uses. The Wired IP is the static IP set above. Currently, the drone is configured to connect to an ad hoc network on our development PC, and the wireless IPs for the devices are in the Dev Hotspot column.

| Device | Wired IP  | Wireless IP (on VOXL Network) | Wireless IP (on DEV Hotspot) |
|--------|-----------|-------------------------------|------------------------------|
|  NUC   | 10.0.0.10 | (Dynamic)                     | 10.42.0.180 (Dynamic)        |
|  VOXL  | 10.0.0.20 | 192.168.8.1 (Default)         | 10.42.0.139 (Dynamic)        |
|  DEV   | N/A       | (Dynamic)                     | 10.42.0.1                    |

Using these, the VOXL can connect to the NUC and vice versa.

To test the connection between the two, run `ping` using the appropriate IP for each client set above.

---
Next, [set up ROS on the VOXL and NUC](ros.md).

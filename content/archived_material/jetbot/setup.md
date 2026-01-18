# JetBot Setup

Your JetBot is starting with (roughly) the [base JetBot image available](https://jetbot.org/master/software_setup/sd_card.html).

## Hardware Overview

The JetBot can be turned on by using the button on the rear left corner, through the hole in the frame. This will turn on the external power bank, supplying power to the single-board computer (Jetson Nano) and the motor power supply board.

Other hardware includes a wide-angle camera (with a lens cap 😛), two wheel/motor assemblies and a roller ball. The single-board computer has a wifi card for connectivity, a small display for debug/configuration info, and an SD card holding the storage for the device.

## Network Setup

In order to connect to the JetBot, your development machine should be connected to the same network as the JetBot. Continue for instructions to do so.

### Making your own network

The JetBot kits have a 2.4GHz wifi card included. Your network/hotspot will need to include the 2.4GHz band, not just the 5GHz.

Firstly, your development machine should be connected to a network (preferrably one you control). The easiest way to do this is to configure your machine to transmit an ad-hoc (hotspot) network. See instructions for [Windows](https://support.microsoft.com/en-us/windows/use-your-windows-pc-as-a-mobile-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85#WindowsVersion=Windows_11), [Mac](https://support.apple.com/guide/mac-help/share-internet-connection-mac-network-users-mchlp1540/mac), or [Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en).

By using an ad-hoc network, you can access your JetBot wherever your development machine works. Alternatively, you can connect it to an existing network, like your home network.

Next, you need to connect your JetBot to your network in one of the following ways:

### Accessing the Shell - Monitor and Keyboard (preferred)

<div class="warning">
As a note, you can come to the Project Office hours and utilize our monitor/keyboards or access the CS computer lab (Devon Energy Hall 115) if you have contacted the CS department for keycard access.
</div>

If you have access to an external monitor and keyboard, you can use it to configure the JetBot to connect to your development network. Simply turn on your JetBot and connect the peripherals to the ports on the robot. This will allow you to access the headless UI (just a console).

Log in via the default credentials (username/password: `jetbot`) and utilize `nmcli` to view nearby networks and connect to yours ([Stack Exchange instructions](https://askubuntu.com/questions/377687/how-do-i-connect-to-a-wifi-network-using-nmcli)).

Ensure your JetBot is connected via the onboard display, which should show an assigned IP beside `wlan`, showing that your device is connected and has received an IP.

### Accessing the Shell - USB

If you are unable to get access to a monitor/keyboard within your development network, utilize [Nvidia's instructions for Wi-Fi Setup](https://jetbot.org/master/software_setup/wifi_setup.html) with USB Device Mode.

### Accessing JupyterLab

Once your development computer and your JetBot are connected to the same network, you can access the JupyterLab environment. This handy tool is hosted by the JetBot and encapsulates file management, terminal access, and running Python notebooks, all within a web interface, so no need to SSH/SFTP/etc.

Just access the JupyterLab in your browser at `http://<wlan IP>:8888`, filling in the IP displayed on the JetBot's display (e.g. `http://192.168.1.2:8888`). The default password for JupyterLab here is also `jetbot`.

### Getting Started

Then, you can proceed through some of the Notebooks to get used to utilizing the environment, the basic JetBot API and ensure that you can control the JetBot remotely using your Bluetooth controller (useful for generating training data later, also just pretty fun).

You can find these notebooks in `~/Notebooks/`, namely `basic_motion.ipynb` and `teleoperation.ipynb`.

Once you are comfortable with the environment, continue to [Machine Learning](ML.html).

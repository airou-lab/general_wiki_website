---
Type:
  - arcProDocs
Labs:
  - AIROU
---
# VESC Setup and unbricking

- VESC type: [Mini FSESC4.20 50A base on VESC® 4.12 with Aluminum Anodized Heat Sink](https://www.flipskyo.com/products/mini-fsesc4-20-50a-with-anodized-heat-sink)
- Github vesc page: [vedderb/bldc: The VESC motor control firmware](https://github.com/vedderb/bldc)

## Setup
1) Download the the vesc tool
2) Turn car upside down and do foc detection with small inrunner (200g) with full vesc battery  
3) Set MotorSettings/Advanced/Maximum_input_voltage to 6.2V   
4) Set AppSettings/General/EnableServoOutput to TRUE (very important cannot turn car without this)  
5) Write app config and motor settings to VESC  

We also tried the following settings:
- Medium inrunner motor
- Cells in Series: 6 cells
- 3aH (or 3k mAh)
- 52mm wheel
	- 4 motor pole
	- no tempature sensor


> [!Warning] Old board setup
    > - For current limit, select general -> voltage, cut start at 8.4, cutoff end at 6v. 
    > - We used to have to erase the registers for the bootloader (certain values), but with a complete earase 
# Unbricking (Red AND blue light flashing)
> [!warning] Red flashing LED vesc
> Under volt error, copy the settings from one of the other robots onto this one..
## Connecting
1) Use the ST Link looks like [this](https://www.adafruit.com/product/2548) 
2) Download the [following](https://www.st.com/en/development-tools/stm32cubeprog.html) and open
3) Connect the pins using a female-female wire as per below, note that only RST,DIO,CKK needs to be connected 
    ![pinout diagarm](https://cdn.shopify.com/s/files/1/0011/4039/1996/files/f4b3da9554de4e60ffd11b8edcb16ff8_15f6cbdf-ff11-4536-a14c-dcf40b80fea6.jpg?v=1735198613)
	1) In this case, `NC` =  DO NOT USE, `-` = GRND
	2) the 3.3V in was not used
4) Connect using the STM32 cubeprog and reflash

Next steps:
[[YDLidar X4 Pro and 435i realsense]]
# Hardware

The hardware is based on the MIT Aerospace Control Lab's [nx Platform](https://gitlab.com/mit-acl/fsw/vehicle-builds/nx). Also see [their list of parts](https://docs.google.com/spreadsheets/d/1Wlv0AggwJEXu4AvRRExc7lY3p_MQ_X4-Evwyve9mzvk/edit#gid=0).

## Components
Below is a comprehensive list of the parts used to build the drone platform.

|    Section     |              Part Name               |
|----------------|--------------------------------------|
|     Frame      | Frame Kit w/ PCB Central Plate ([S550 Frame Kit](https://www.littohot.com/products/s550-hexacopter-frame-kit-with-pcb-central-plate-s550pcb)) |
|                | Custom 3D-Printed Body               |
|                | Custom 3D-Printed Body-PCB Interface |
|                | Custom 3D-Printed Legs               | 
| Motor Assembly | Motors (6x [FLASH HOBBY D2836 1500KV](https://a.co/d/2fDZAUj))                          |
|                | Propellers (6x)                      |
|                | Electronic Speed Controllers (6x [QWinOut 2-4S 30A ESC](https://www.amazon.com/QWinOut-Brushless-Controller-Multicopter-Quadcopter/dp/B07SFLJJQ5?th=1)) |
|  Computation   | VOXL Flight Deck                     |
|                | Intel NUC (NUC11PAHi7)               |
|  Power Supply  | LiPo Battery ([5200 mAh, 11.1V](https://www.amazon.com/HOOVO-Battery-5200mAh-Helicopter-Airplane/dp/B08V8YCZFF/ref=sr_1_26?))  |
|                | Voltage Step-Up Board  ([150W DC-DC 19V](https://www.amazon.com/Gowoops-10-32V-Converter-Adjustable-Voltage/dp/B00J1X4XXM/ref=sr_1_26?))              |
|                | Power Distribution Board ([MATEK XT60 PDB](https://www.amazon.com/MATEK-Distribution-PDB-XT60-Quadcopter-QAV210/dp/B07QPW14KK)) |
| Remote Control | Receiver (SPM9745 DSMX)              |
|                | Transmitter/Controller (DXS SPM1010) |

As a note, the parts used from the frame kit are:
* Central PCB top plate
* Central PCB bottom plate
* Injection moulded arms (x6)

## 3D printing
A [zip containing the STL files](../stl/AIROU-Drone-STLs.zip) for the project is available for download.

As a note, the landing gear (`Landing Gear.STL`) was printed in flexible TPU and the main base (`Couple Base.STL`) in rigid PETG. The rest was printed in PLA.
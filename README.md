# R2-D2

美術の自由制作の授業で作成した、簡易ロボットの動作に使われたコード。

## Features

* モーターを操作しロボットを前後に動かす
* 目のLEDライトのOn/Off
* ブラウザから操作可能

## How to setup

1. Connect pins of motor, IC tip for motor-control, and LED to appropriate GPIO pins.
2. Clone this repository to somewhere on Raspberry Pi.
3. Execute `npm install` to install required node package.
4. Execute `node index.js` to run. You can use R2-D2 Controller by accessing to port 3000 of Raspberry Pi IP Address.

## Required Environment

* Hardware (Description of how to connect is omitted on this page, sorry)
    - Raspberry Pi
    - Motor
    - 2 alkaline batteries
    - Motor Controller (Confirmed: L293D)
* Software
    - Raspbian (Debian Jessie Base)  
You can also run this on Raspbian of Debian Wheezy base, but root permission will be required to run Python program for controlling GPIO pins.
    - nodejs and npm  
Any version will do, but latest version is recommended.

# Motion sensor camera

## Brief
This simple project aims to take a picture when motion is detected and save the picture to the USB flash drive.

## HW
The device is powered by Raspberry Pi 3 or other which includes the camera interface. For taking pictures is used the originar Raspberry Pi Camera module. For motion sensing is used PIR sensor HC-SR501.


## SW
This project uses two scripts. The python script interfaces the sensor and if motion is detected, it runs the bash script which takes photo using raspistill tool. The taken photo has date and time in its name and is moved to the plugged-in USB drive which must be named drive01. On the USB drive is created directory "photos" and all taken photos are placed there along with the application log "output.txt".


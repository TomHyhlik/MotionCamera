#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
DIRECTORY="/media/pi/drive01/photos/"

if [ -d /media/pi/02drive/ ]; then
	if [ ! -d "$DIRECTORY" ]; then
		echo the directory "$DIRECTORY" does not exist		>> output.txt
		echo creating the "$DIRECTORY" directory...		>> output.txt
		mkdir "$DIRECTORY"
	fi
	raspistill -vf -hf -o $DATE.jpg 				&>> output.txt
	mv $DATE.jpg  "$DIRECTORY" 					&>> output.txt
	echo photo $DATE.jpg succesfully taken				>> output.txt
	cp output.txt "$DIRECTORY"					&>> output.txt
else
	echo 01drive is not plugged in 					>> output.txt
fi
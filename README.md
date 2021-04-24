![](https://raw.githubusercontent.com/nnnnnzo/Quantum-Vladimir/main/Assets/badge.png)
## *Vladimir is my co-pilot* (project for last year of HighSchool engineering sciences)
<br>A Yolov2 neural network used to pilot rbpi from SL-5 (a squash ball launcher) over a network using sockets.

## a very comprehensive drawing to explain the thingy
![](https://raw.githubusercontent.com/nnnnnzo/Quantum-Vladimir/main/Assets/Schema%20lol.png)
![](https://raw.githubusercontent.com/nnnnnzo/Quantum-Vladimir/main/Assets/RealisticFragrantHerculesbeetle-size_restricted.gif)
<br>All of this is done just to run the neural network on another computer because on the rbpi, he burn 🔥
btw the goal is to follow a person with the cam/cannon so we send x and y pos to the rbpi and he turn the 
motor to always face the person 🔫. (code not out yet; Iam working on it) 

## so far so good
So I just made the thing running and I got very good result in terms of delay/latency wich was making the software unusable on the pi,
you can see it with this very scientist data graph 🧪: (these times values are **ΔT=t2-t1** with **t1 = person in the field of view** and **t2 = x and y data reaching the pi**)
<br>![](https://raw.githubusercontent.com/nnnnnzo/Quantum-Vladimir/main/Assets/Delay%20in%20milliseconds%20(RBPI%204%20with%204GB%20ram)-2.png)
<br>***I don't have data for [RBPI + MacBookAir with Yolo + Picamera Video Stream] because I don't have the Picamera (csi) at home***
<br>As you can see, the all thing is much faster ⚡️ and can be use to follow a person using the motor.
<br>![](https://raw.githubusercontent.com/nnnnnzo/Quantum-Vladimir/main/Assets/i49pmy0yqe4l.gif)
<br>*gotta go fast*

## mid state 🐥
The code uploaded is a middle state one, it does not handle an video stream on the network due to the fact that I dont currently have a PiCamera
<br>* ***Server.py*** run on the rbpi
<br>* ***Vision.py*** run on the computer that will handle the neural network and image detection
<br>*(port 9093, and need the yolov2-tiny [weights](https://pjreddie.com/media/files/yolov2-tiny.weights) and [cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov2-tiny.cfg) files)*

## License

[![GNU GPLv3 Logo](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

Quantum-Vladimir is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

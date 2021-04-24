import cv2
import numpy as np
from colorama import Fore, Back, Style
import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Load Yolo
net = cv2.dnn.readNet("yolov2-tiny.weights", "yolov2-tiny.cfg")
#net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")
classes = []
print("RBPI IP ?")
u_ip = str(input())
clientSocket.connect((u_ip,9093));
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
label = ''
intopt = 0

print("press enter to start without args")

C_mod = (input())
if C_mod == "" or C_mod == "-b":
    intopt = 0.54
elif C_mod == "-a":
    intopt = 0.3
elif C_mod == "-m":
    intopt = 0.01
    

# Loading video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("the_new_video_is.avi", fourcc , 5, (640, 360))

# repalce the test.mp4 with an video of your own 
camera = cv2.VideoCapture(0)

while True:
    _,img = camera.read()
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    prct = 0
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > intopt:
                ff = 0
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                #print(class_ids) #nombre d'objet écran bof
                prct = round(confidence * 100,1)
                if label == 'person':
                    print(Style.BRIGHT, Fore.GREEN + 'person', prct,"%", "|  X:",x,"Y:",y)
                    data = str(x);
                    clientSocket.send(data.encode());
                else:
                    print(label, prct,"%", "|  X:",x,"Y:",y)
                

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            if label == 'person':
                color = (0, 255, 0)
            else :
                color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 6)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            cv2.putText(img, str(prct)+"%", (x, y + 70), font, 3, color, 3)

    cv2.imshow("Vision", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()

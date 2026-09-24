#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput

import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

image = jetson.utils.videoSource("/home/nvidia/Desktop/person.jpeg")

display = jetson.utils.videoOutput("/home/nvidia/Desktop/person_result.jpg")

while display.IsStreaming():

    img = image.Capture()

    if img is None:
        continue

    detections = net.Detect(img)

    print(detections)

    display.Render(img)

    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))



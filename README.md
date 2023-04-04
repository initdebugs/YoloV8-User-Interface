# YoloV8 User Interface
This is a simple user interface for YOLOv8, a popular object detection system. The user can select a video or image file and a YOLO model file, and then run YOLO on the selected input using the specified model. The output of YOLO is displayed in the GUI window, along with a progress bar that updates as YOLO processes the input.

![image](https://user-images.githubusercontent.com/75781464/229143183-3ed5c44f-aee6-44bf-b40d-4425a0fea452.png)

# Installation
To use this program, you will need to install Python 3 and several Python packages. You can do this using the following commands:

```pip install PySimpleGUI Ultralytics```

# Usage
To run the program, simply run the main.py file:
```python main.py```

Once the program is running, please select if you want to start a Training or Detection.

Training:

At first, select if you want to create an Object Detection model or a Segmentation model (remember to select the one fitting for your dataset and annotation format). Then, select the .yaml file for your dataset. Please choose which model size you want: s is smallest (faster training and interference, lowest accuracy), x is biggest (slower training and interference, highest accuracy). Also choose how many epochs you want to train. To start the training, press the Train button. This will run YOLO on the selected dataset with the provided parameters.

Detection:

At first, select if you want to do Object Detection or Segmentation (remember to use the correct model type). You can use the "Browse Video/Image" and "Browse Model" buttons to select the input video/image and the YOLO model file, respectively. You can also choose whether to use the GPU for processing and whether to show the output in a window using the checkboxes.
To start processing, click the "Process" button. This will run YOLO on the selected input using the specified model.

# Pretrained models
This section shows a table of some models I trained myself using YoloV8. You can download these and use in the User Interface.

Object detection models:
| Model  | Link |
| ------------------------ | ------------------------------------- |
| TrafficDetection_8S  | [Google Drive](https://drive.google.com/file/d/1m80nfw0tL2YvvuuGHnY8sKSmQhPUNXbM/view?usp=sharing)  |
| TrafficDetection_8L  | [Google Drive](https://drive.google.com/file/d/1LXTksK0M2R_JQQ6bXpetJWJl9neO4JC5/view?usp=sharing)  |
| DollarBillDetection_8S | [Google Drive](https://drive.google.com/file/d/1VMpCFZ7lEf7ksPKyKSZbX5x--4ET_qHx/view?usp=sharing)|
| FurnitureDetection_8S | [Google Drive](https://drive.google.com/file/d/1GHP0myTllmi-MKUPGEyzl_IjBmWNJNgp/view?usp=sharing) |

Segmenation models:
| Model  | Link |
| ------------------------ | ------------------------------------- |
| RoadSegmentation_8S  | [Google Drive](https://drive.google.com/file/d/1WS3rS4DNaERCqwaHVQE7VD0nt3mt2lUi/view?usp=sharing)  |

Models:

TrafficDetection: The Traffic Detection model detects common traffic objects. Such as cars, trucks, pedestrians, common traffic signs, traffic lights. This model is trained on my own dataset. [Roboflow project](https://app.roboflow.com/lesley-natrop-zgywz/traffic-detection-e3og7/5)

RoadSegmentation: The Road Detection model detects the road in dashcam videos and overlays it using Instance Segmentation. This model is trained on my own dataset. [Roboflow project](https://app.roboflow.com/lesley-natrop-zgywz/road-detection-segmentation/7)

DollarBillDetection: The Dollar Bill Detection model recognizes different American Dollar bills. This model is trained by me. I used the dataset created by [Alex Hyams](https://universe.roboflow.com/alex-hyams-cosqx) on Roboflow. [Roboflow Project](https://universe.roboflow.com/alex-hyams-cosqx/dollar-bill-detection)

FurnitureDetection: The Furniture Detection model detects several different kinds of furniture, such as tables, chairs, etc. The model is trained by me. I used the dataset created by [Roboflow 100](https://universe.roboflow.com/roboflow-100) on Roboflow. [Roboflow Project](https://universe.roboflow.com/roboflow-100/furniture-ngpea)

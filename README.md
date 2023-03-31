# YoloV8 User Interface
This is a simple user interface for YOLOv8, a popular object detection system. The user can select a video or image file and a YOLO model file, and then run YOLO on the selected input using the specified model. The output of YOLO is displayed in the GUI window, along with a progress bar that updates as YOLO processes the input.

# Installation
To use this program, you will need to install Python 3 and several Python packages. You can do this using the following commands:

```pip install PySimpleGUI Ultralytics```

# Usage
To run the program, simply run the main.py file:
```python main.py```

Once the program is running, you can use the "Browse Video/Image" and "Browse Model" buttons to select the input video/image and the YOLO model file, respectively. You can also choose whether to use the GPU for processing and whether to show the output in a window using the checkboxes.

To start processing, click the "Process" button. This will run YOLO on the selected input using the specified model. The output of YOLO will be displayed in the output window, and the progress bar will update as YOLO processes the input.

# Pretrained models
This section shows a table of some models I trained myself using YoloV8. You can download these and use in the User Interface.
| Model  | Link |
| ------------------------ | ------------------------------------- |
| TrafficDetection_8S - The Traffic Detection model detects common traffic objects. Such as cars, trucks, pedestrians, common traffic signs, traffic lights.   | [Google Drive](https://drive.google.com/file/d/1m80nfw0tL2YvvuuGHnY8sKSmQhPUNXbM/view?usp=sharing)  |
| TrafficDetection_8L - The Traffic Detection model detects common traffic objects. Such as cars, trucks, pedestrians, common traffic signs, traffic lights.   | [Google Drive](https://drive.google.com/file/d/1LXTksK0M2R_JQQ6bXpetJWJl9neO4JC5/view?usp=sharing)  |

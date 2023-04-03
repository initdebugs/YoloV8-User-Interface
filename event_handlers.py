import os
from threading import Thread
import queue
import re
from yolo_functions import execute_yolo_command, update_progress

def handle_first_page_events(event, values):
    if event == 'Next':
        return values['training_radio'], values['detection_radio']

def handle_training_page_events(event, values, window, yolo_thread, output_queue):
    if event == 'Train':
        return train_yolo(window, values, yolo_thread, output_queue)
        
def handle_detection_page_events(event, values, window, yolo_thread, output_queue):
    if event == 'Process':
        return process_yolo(window, values, yolo_thread, output_queue)

def train_yolo(window, values, yolo_thread, output_queue):
    yaml_path = values['yaml']

    if not os.path.isfile(yaml_path):
        window['status'].update('Error: Invalid YAML path.')
        return

    detection_type = 'segment' if values['segmentation'] else 'detect'
    model_size = 'n' if values['model_n'] else 's' if values['model_s'] else 'm' if values['model_m'] else 'l' if values['model_l'] else 'x'
    model_name = f'yolov8{model_size}-seg.pt' if detection_type == 'segment' else f'yolov8{model_size}.pt'
    epochs = values['epochs']

    command = f'yolo task={detection_type} mode=train model="{model_name}" data="{yaml_path}" epochs={epochs}'

    yolo_thread = Thread(target=execute_yolo_command, args=(command, output_queue), daemon=True)
    yolo_thread.start()

    window['Train'].update(visible=False)

    while not output_queue.empty():
        line = output_queue.get()
        if line is None:
            window['Train'].update(visible=True)
        else:
            print(line)
            update_progress(window, line)

def process_yolo(window, values, yolo_thread, output_queue):
    video_path = values['video']
    model_path = values['model']

    if not os.path.isfile(video_path):
        window['status'].update('Error: Invalid video/image path.')
        return

    if not os.path.isfile(model_path):
        window['status'].update('Error: Invalid model path.')
        return

    detection_mode = 'segment' if values['segmentation'] else 'detect'
    device = '0' if values['gpu'] else 'cpu'
    show = str(values['show']).lower()
    command = f'yolo task={detection_mode} mode=predict model="{model_path}" source="{video_path}" device={device} show={show}'

    yolo_thread = Thread(target=execute_yolo_command, args=(command, output_queue), daemon=True)
    yolo_thread.start()

    window['Process'].update(visible=False)

    while not output_queue.empty():
        line = output_queue.get()
        if line is None:
            window['Process'].update(visible=True)
        else:
            print(line)
            update_progress(window, line)

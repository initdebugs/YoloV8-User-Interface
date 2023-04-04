import os
from threading import Thread
import queue
import re
from yolo_functions import execute_yolo_command, update_progress
import PySimpleGUI as sg

def handle_first_page_events(event, values):
    is_training = False
    is_detection = False

    if event == 'Next':
        if values['training_radio']:
            is_training = True
        elif values['detection_radio']:
            is_detection = True

    return is_training, is_detection

def handle_training_page_events(event, values, window, yolo_thread, output_queue):
    if event == 'Train':
        yaml_path = values['yaml']

        if not os.path.isfile(yaml_path):
            window['status'].update('Error: Invalid YAML path.')
            sg.popup_error('Invalid YAML path. Please provide a valid YAML file.')
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
            print(line)  # This line will print the output to the console
            update_progress(window, line)

def handle_detection_page_events(event, values, window, yolo_thread, output_queue):
    if event == 'Process':
        video_path = values['video']
        model_path = values['model']

        if not os.path.isfile(video_path):
            window['status'].update('Error: Invalid video/image path.')
            sg.popup_error('Invalid video/image path. Please provide a valid video or image file.')
            return

        if not os.path.isfile(model_path):
            window['status'].update('Error: Invalid model path.')
            sg.popup_error('Invalid model path. Please provide a valid model file.')
            return

        detection_mode = 'segment' if values['segmentation'] else 'detect'
        device = '0' if values['gpu'] else 'cpu'
        show = str(values['show']).lower()
        selected_options = values['dropdown_options']
        hide_labels = 'True' if 'Hide labels' in selected_options else 'False'
        hide_confidence = 'True' if 'Hide confidence' in selected_options else 'False'


        command = f'yolo task={detection_mode} mode=predict save=True model="{model_path}" source="{video_path}" device={device} show={show} hide_labels={hide_labels} hide_conf={hide_confidence}'

        yolo_thread = Thread(target=execute_yolo_command, args=(command, output_queue), daemon=True)
        yolo_thread.start()

        window['Process'].update(visible=False)

    while not output_queue.empty():
        line = output_queue.get()
        if line is None:
            window['Process'].update(visible=True)
        else:
            print(line)  # This line will print the output to the console
            progress = update_progress(window, line)
            if progress is not None:
                window['progress_percentage'].update(f'{progress}%')

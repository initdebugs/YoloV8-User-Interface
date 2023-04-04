import PySimpleGUI as sg

def first_page_layout():
    layout = [
        [sg.Radio('Training', "RADIO1", default=True, key='training_radio', tooltip='Select to switch to training mode')],
        [sg.Radio('Detection', "RADIO1", key='detection_radio', tooltip='Select to switch to detection mode')],
        [sg.Button('Next'), sg.Button('Cancel')]
    ]
    return layout

def training_page_layout():
    layout = [
        [sg.Radio('Object Detection', "RADIO2", default=True, key='object_detection', tooltip='Perform object detection'), sg.Radio('Segmentation', "RADIO2", key='segmentation', tooltip='Perform image segmentation')],
        [sg.InputText(key='yaml', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse YAML', file_types=(('YAML Files', '*.yaml'), ('All Files', '*.*')), tooltip='Choose a YAML file for the dataset')],
        [sg.Radio('n', "RADIO3", default=True, key='model_n', tooltip='Select model size n'), sg.Radio('s', "RADIO3", key='model_s', tooltip='Select model size s'), sg.Radio('m', "RADIO3", key='model_m', tooltip='Select model size m'), sg.Radio('l', "RADIO3", key='model_l', tooltip='Select model size l'), sg.Radio('x', "RADIO3", key='model_x', tooltip='Select model size x')],
        [sg.Text('Epochs:'), sg.InputText(key='epochs', size=(5, 1), do_not_clear=True, enable_events=True, tooltip='Enter the number of epochs')],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progress'), sg.Text('0%', key='progress_percentage', size=(5, 1))],
        [sg.Button('Train', tooltip='Start training'), sg.Button('Back', tooltip='Go back to the first page'), sg.Button('Cancel', tooltip='Cancel and close the application')]
    ]
    return layout

def detection_page_layout():
    layout = [
        [sg.Radio('Object Detection', "RADIO2", default=True, key='object_detection', tooltip='Perform object detection'), sg.Radio('Segmentation', "RADIO2", key='segmentation', tooltip='Perform image segmentation')],
        [sg.InputText(key='video', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Video/Image', file_types=(('Video Files', '*.mp4'), ('Image Files', '*.jpg *.jpeg *.png'), ('All Files', '*.*')), tooltip='Choose a video or image file')],
        [sg.InputText(key='model', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Model', tooltip='Choose a model file')],
        [sg.Text('Extra options:'),sg.Listbox(['Hide labels', 'Hide confidence'], key='dropdown_options', size=(20, 2), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, enable_events=True, tooltip='Select extra options for object detection or segmentation')],
        [sg.Checkbox('Use GPU', key='gpu', tooltip='Use GPU for processing'), sg.Checkbox('Show', key='show', tooltip='Show the detection/segmentation results')],
        [sg.Button('Process', tooltip='Start processing the video/image'), sg.Text('', key='status', size=(50, 1))],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progress'), sg.Text('0%', key='progress_percentage', size=(5, 1))],
        [sg.Button('Back', tooltip='Go back to the first page'), sg.Button('Cancel', tooltip='Cancel and close the application')]
    ]
    return layout


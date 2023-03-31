import os
import subprocess
import PySimpleGUI as sg
from threading import Thread
import queue
import re

def execute_yolo_command(command, output_queue):
    output_queue.put(command)
    print(command)
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        for line in iter(process.stdout.readline, b''):
            line = line.decode("utf-8").strip()
            output_queue.put(line)

        process.stdout.close()
        process.wait()
        output_queue.put(None)
    except Exception as e:
        output_queue.put(f'Error: {e}')
        output_queue.put(None)

def update_progress(window, line):
    match = re.search(r'\((\d+)/(\d+)\)', line)
    if match:
        current_frame, total_frames = int(match.group(1)), int(match.group(2))
        progress = int(current_frame / total_frames * 100)
        window['progress'].update(progress)

def browse_file(file_types):
    return sg.popup_get_file('Select a file', file_types=file_types)

def main():
    sg.theme('Tan')

    layout = [
        [sg.InputText(key='video', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Video/Image', file_types=(('Video Files', '*.mp4'), ('Image Files', '*.jpg *.jpeg *.png'), ('All Files', '*.*')))],
        [sg.InputText(key='model', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Model')],
        [sg.Checkbox('Use GPU', key='gpu'), sg.Checkbox('Show', key='show')],
        [sg.Button('Process'), sg.Text('', key='status', size=(50, 1))],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progress')]
    ]

    window = sg.Window('YoloV8 User Interface', layout, finalize=True)

    output_visible = True
    yolo_thread = None
    output_queue = queue.Queue()

    while True:
        # Wait for an event (e.g. button press or window close)
        event, values = window.read(timeout=100)

        if event in (sg.WIN_CLOSED, 'Exit'):
            # If the window is closed or the 'Exit' button is pressed, exit the loop and close the window
            break

        if event == 'Process':
            # If the 'Process' button is pressed, start running YOLO on the selected video/image and model
            video_path = values['video']
            model_path = values['model']

            # Check that the video/image and model files exist
            if not os.path.isfile(video_path):
                window['status'].update('Error: Invalid video/image path.')
                continue

            if not os.path.isfile(model_path):
                window['status'].update('Error: Invalid model path.')
                continue

            # Build the YOLO command based on the selected options
            device = '0' if values['gpu'] else 'cpu'
            show = str(values['show']).lower()
            command = f'yolo task=detect mode=predict model="{model_path}" source="{video_path}" device={device} show={show}'

            # Start running YOLO in a separate thread
            yolo_thread = Thread(target=execute_yolo_command, args=(command, output_queue), daemon=True)
            yolo_thread.start()

            # Disable the 'Process' button while YOLO is running
            window['Process'].update(visible=False)

        # Check for new output from YOLO and update the GUI accordingly
        while not output_queue.empty():
            line = output_queue.get()
            if line is None:
                # If the output is complete, enable the 'Process' button again
                window['Process'].update(visible=True)
            else:
                # If the output is not complete, add the line to the GUI output window and update the progress bar
                print(line)  # This line will print the output to the console
                update_progress(window, line)

    # Close the GUI window
    window.close()


    window.close()

if __name__ == '__main__':
    main()
import PySimpleGUI as sg
from layouts import first_page_layout, training_page_layout, detection_page_layout
from event_handlers import handle_first_page_events, handle_training_page_events, handle_detection_page_events
from threading import Thread
import queue

def main():
    sg.theme('Tan')

    # Initialize layouts and windows
    first_page = first_page_layout()
    window1 = sg.Window('YoloV8 User Interface - Choose Mode', first_page, finalize=True, size=(600, 220))

    while True:
        event1, values1 = window1.read()
        is_training, is_detection = handle_first_page_events(event1, values1)

        if event1 == 'Next':
            window1.close()
            if is_training or is_detection:
                break
        elif event1 in (sg.WIN_CLOSED, 'Cancel'):
            window1.close()
            return

    if is_training:
        training_page = training_page_layout()
        window2 = sg.Window('YoloV8 User Interface - Training', training_page, finalize=True, size=(600, 220))

        yolo_thread = None
        output_queue = queue.Queue()

        while True:
            event2, values2 = window2.read(timeout=100)
            handle_training_page_events(event2, values2, window2, yolo_thread, output_queue)

            if event2 in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
                break
            elif event2 == 'Back':
                window2.close()
                main()
                break

        window2.close()

    elif is_detection:
        detection_page = detection_page_layout()
        window2 = sg.Window('YoloV8 User Interface - Detection', detection_page, finalize=True, size=(600, 220))

        yolo_thread = None
        output_queue = queue.Queue()

        while True:
            event2, values2 = window2.read(timeout=100)
            handle_detection_page_events(event2, values2, window2, yolo_thread, output_queue)

            if event2 in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
                break
            elif event2 == 'Back':
                window2.close()
                main()
                break

        window2.close()

if __name__ == '__main__':
    main()
